#!/usr/bin/env bash
## Author: Ondřej Profant
## Licence: GPL
## Dependencies: pandoc, zenity, vlna
## Install into:
## - ~/.local/share/nautilus/scripts/ (Fedora, Ubuntu)

# Global vars
bin=pandoc
output=""
tmpdir=".md2pdf-textmpdir"
errorFile=".md2pdf-errors.txt"

function end() {
        rm -rf "$tmpdir"
        zenity --text "$1" --error;
        exit 1
}

function input() {
        if [ -z "$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS" ]; then
                echo "Nautilus does not pass any data, use readme instead"
                NAUTILUS_SCRIPT_SELECTED_FILE_PATHS=("readme.md" "readme 2.md")
                cp "readme.md" "readme 2.md"
        fi;
        file1="${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS[0]}"
        file=$(basename "$file1")
        output="${file%.*}.pdf"
}

function convert() {

        if $bin -v > /dev/null; then
                mkdir -p "$tmpdir"

                # Todo: multiple files input
                files=$(basename "${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS[0]}")
                $bin -f markdown -t latex --latex-engine=xelatex \
                        --smart --normalize -s \
                        -o - "$files" \
                        2> "$errorFile" | \
                vlna -f -r -v KkSsVvZzOoUuAaI 2>> "$errorFile" | \
                xelatex -output-directory="$tmpdir" >> "$errorFile" 2>&1; \
                rets=(${PIPESTATUS[*]})

                if [ ${rets[0]} -ne 0 ]; then
                        end "Pandoc returns code ${rets[0]} for: $files ($output), more info in file: $errorFile"
                fi;
                if [ ${rets[1]} -ne 0 ]; then
                        end "vlna returns code ${rets[1]} for: $files ($output), more info in file: $errorFile"
                fi;
                if [ ${rets[2]} -ne 0 ]; then
                        end "xelatex returns code ${rets[2]} for: $files ($output), more info in file: $errorFile"
                fi;

                mv "$tmpdir/texput.pdf" "$output"
                rm "$errorFile"
                rm -rf "$tmpdir"
                
        else
                end "Pandoc not found, path: $bin"
        fi;
}

input
convert
