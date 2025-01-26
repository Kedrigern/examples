using System;
using System.Drawing;
using System.Windows.Forms;

namespace pacman
{
	public class AppMenu : MenuStrip
	{
		Bitmap newICO   ;
		Bitmap pauseICO ;
		Bitmap exitICO  ;
		Bitmap openICO  ;
		Bitmap aboutICO ;
		Bitmap setingsICO;

		private ToolStripMenuItem sizeCH;

		public AppMenu(EventHandler NG, EventHandler Pausa, EventHandler CHsp, EventHandler Chmap, EventHandler Resize) : base()
		{	
			this.Visible = true;

			try {		
				this.newICO   = new Bitmap(Settings.newICO);
				this.pauseICO = new Bitmap(Settings.pauseICO);
				this.exitICO  = new Bitmap(Settings.exitICO);
				this.openICO  = new Bitmap(Settings.openICO);
				this.aboutICO = new Bitmap(Settings.aboutICO);
				this.setingsICO = new Bitmap(Settings.setingsICO);
			} catch 
			{
				this.newICO = new Bitmap(16,16);
				this.pauseICO = new Bitmap(16,16);
				this.exitICO  = new Bitmap(16,16);
				this.openICO  = new Bitmap(16,16);
				this.aboutICO = new Bitmap(16,16);
				this.setingsICO = new Bitmap(16,16);
				MessageBox.Show("No icons in GTK share files...", "No icons",
					MessageBoxButtons.OK, MessageBoxIcon.Error);
			}

			ToolStripMenuItem game = new ToolStripMenuItem("Game"); 
			this.Items.Add(game);
			ToolStripMenuItem newgame = new ToolStripMenuItem("New game", newICO, NG);	     
			newgame.ShortcutKeys = (Keys) Shortcut.CtrlN;
			newgame.ShowShortcutKeys = true;
			game.DropDownItems.Add(newgame); 
			ToolStripMenuItem pauseM = new ToolStripMenuItem("Pause", pauseICO, Pausa);
			pauseM.ShortcutKeys = (Keys) Shortcut.CtrlP;
			game.DropDownItems.Add(pauseM);
			ToolStripMenuItem exit = new ToolStripMenuItem("Exit", exitICO, this.OnExit);
			exit.ShortcutKeys = (Keys) Shortcut.CtrlQ;
			exit.ShowShortcutKeys = true;
			game.DropDownItems.Add(exit);

			ToolStripMenuItem seting = new ToolStripMenuItem("Settings"); 
			this.Items.Add(seting);
			ToolStripMenuItem CHmap = new ToolStripMenuItem("Change map", openICO, Chmap);
			CHmap.ShortcutKeys = (Keys) Shortcut.CtrlM;
			seting.DropDownItems.Add(CHmap);
			ToolStripMenuItem CHspeed = new ToolStripMenuItem("Change speed", setingsICO, CHsp);
			seting.DropDownItems.Add(CHspeed);
			this.sizeCH = new ToolStripMenuItem("Small");
			sizeCH.ShortcutKeys = (Keys) Shortcut.CtrlS;
			seting.DropDownItems.Add(sizeCH);
			sizeCH.Checked = false;
			sizeCH.Click += new EventHandler( Resize );
			sizeCH.Click += new EventHandler( this.Check );

			ToolStripMenuItem about = new ToolStripMenuItem("About");
			this.Items.Add(about);
			ToolStripMenuItem pacmanMENU = new ToolStripMenuItem("Pacman", aboutICO, AboutGame);		
			about.DropDownItems.Add(pacmanMENU);
			ToolStripMenuItem author = new ToolStripMenuItem("Authors", aboutICO, AboutAuthor);		
			about.DropDownItems.Add(author);

		}

		private void Check(object sender, EventArgs e) {
			if (this.sizeCH.Checked) 
				this.sizeCH.Checked = false;
			else this.sizeCH.Checked = true;
		}

		public void AboutGame(object sender, EventArgs e)
		{
			MessageBox.Show("PacMan je zápočtový program.\nCode create with VIM and MonoDevelop\nGraphics create with Gimp.", 
				"about PacMan",
				MessageBoxButtons.OK, MessageBoxIcon.Information);
		}

		public void AboutAuthor(object sender, EventArgs e)
		{
			MessageBox.Show("Code: Ondrej Profant \n  http://www.anilinux.org/~keddie\n\n" +
				"Graphics: \n Lada Svadlenkova\n Ondrej Profant", 
				"about Authors",
				MessageBoxButtons.OK, MessageBoxIcon.Information);
		}

		public void OnExit(object sender, EventArgs e) 	
		{	
			Application.Exit();
		}	
	}
}

