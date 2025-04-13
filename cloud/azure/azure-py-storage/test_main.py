import os
import sys
import pytest
from main import (
    blob_list,
    blob_upload,
    table_set,
    table_get,
    table_list,
    main,
)

# --- Fake clients for blob storage ---


class FakeBlob:
    def __init__(self, name: str) -> None:
        self.name = name


class FakeBlobContainer:
    def __init__(self) -> None:
        self.blobs = [FakeBlob("file1.txt"), FakeBlob("file2.txt")]
        self.uploads = []

    def list_blobs(self):
        return self.blobs

    def upload_blob(self, name: str, data, overwrite: bool) -> None:
        self.uploads.append(name)
        print(f"Fake upload: {name}")

    def get_container_properties(self):
        # Simulace správného získání properties
        pass


# --- Fake client for table storage ---


class FakeTableClient:
    def __init__(self) -> None:
        self.entities = {}

    def upsert_entity(self, entity: dict) -> None:
        self.entities[entity["RowKey"]] = entity
        print(f"Fake upsert: {entity}")

    def get_entity(self, partition_key: str, row_key: str) -> dict:
        if row_key in self.entities:
            return self.entities[row_key]
        else:
            raise Exception("Entity not found")

    def list_entities(self, filter: str):
        # Ignorujeme filtr pro potřeby testu
        return self.entities.values()


# --- Blob Storage tests ---


def test_blob_list(capsys, monkeypatch):
    fake_container = FakeBlobContainer()
    blob_list(fake_container)
    captured = capsys.readouterr().out
    assert "file1.txt" in captured
    assert "file2.txt" in captured


def test_blob_upload(tmp_path, capsys):
    fake_container = FakeBlobContainer()
    # Vytvoříme dočasný soubor
    test_file = tmp_path / "test.txt"
    test_file.write_text("dummy content")
    blob_upload(fake_container, str(test_file))
    captured = capsys.readouterr().out
    assert "Uploaded file 'test.txt'." in captured
    assert "test.txt" in fake_container.uploads


# --- Table Storage tests ---


def test_table_set_and_get(capsys):
    fake_table = FakeTableClient()
    table_set(fake_table, "k1", "v1")
    # Ověříme output upsert
    captured = capsys.readouterr().out
    assert "Set key 'k1' -> 'v1'" in captured or "Fake upsert" in captured

    # Test get
    table_get(fake_table, "k1")
    captured = capsys.readouterr().out
    assert "k1: v1" in captured


def test_table_list(capsys):
    fake_table = FakeTableClient()
    table_set(fake_table, "k1", "v1")
    table_set(fake_table, "k2", "v2")
    # Vyčistíme výstup před voláním list
    capsys.readouterr()
    table_list(fake_table)
    captured = capsys.readouterr().out
    assert "k1: v1" in captured
    assert "k2: v2" in captured


# --- CLI integration tests ---


def test_main_file_list(monkeypatch, capsys):
    # Monkeypatchujeme funkci get_blob_container_client, aby vrátila fake client
    fake_container = FakeBlobContainer()
    monkeypatch.setattr("main.get_blob_container_client", lambda: fake_container)
    monkeypatch.setattr(sys, "argv", ["main.py", "file", "list"])
    main()
    captured = capsys.readouterr().out
    assert "file1.txt" in captured
    assert "file2.txt" in captured


def test_main_val_get(monkeypatch, capsys):
    fake_table = FakeTableClient()
    # Vložíme fake entitu do tabulky
    fake_table.entities["k1"] = {"RowKey": "k1", "Value": "v1"}
    monkeypatch.setattr("main.get_table_client", lambda: fake_table)
    monkeypatch.setattr(sys, "argv", ["main.py", "val", "get", "k1"])
    main()
    captured = capsys.readouterr().out
    assert "k1: v1" in captured


def test_main_val_set(monkeypatch, capsys):
    fake_table = FakeTableClient()
    monkeypatch.setattr("main.get_table_client", lambda: fake_table)
    # Simulujeme vstup od uživatele
    monkeypatch.setattr("builtins.input", lambda prompt: "v1")
    monkeypatch.setattr(sys, "argv", ["main.py", "val", "set", "k1"])
    main()
    captured = capsys.readouterr().out
    assert "Set key 'k1' -> 'v1'" in captured
    # Ověříme, že entita byla vložena
    assert fake_table.entities["k1"]["Value"] == "v1"
