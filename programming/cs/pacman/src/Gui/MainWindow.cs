using System;
using System.ComponentModel;
using System.Windows.Forms;
using System.Drawing;

namespace pacman
{
	public class MainWindow : Form
	{
		private IContainer components;
		private Timer timer;
		private Bitmap gameover;
		private Bitmap gamewin;
		public Speed actualSpeed;
		private bool pause;
		private bool IsDraw;
		private int wait;
		public bool revenge;
		public bool bonusIs;
		private int revengeTime;

		private Map newMap;	// Temporaly map
		private Map mapa;
		private Pacman pac;

		private int sizeField;

		private AppMenu MyMymenu;
		private	StatusBar SB;

		#region /* Declaration of size */
		public int PlaygroundWidth 		;		
		public int PlaygroundHeight     ;			
		#endregion

		public static void Main ()
		{	
			Application.Run (new MainWindow ());
		}

		public MainWindow() : base()
		{			
			components = new Container();
			this.sizeField = 40;
			this.actualSpeed = pacman.Speed.medium;
			this.revenge = false;
			this.bonusIs = true;
			this.IsDraw = false;
			try{
				this.gamewin = new Bitmap( System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.game.win.png" ));
				this.gameover = new Bitmap( System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.game.over.png"));
			} catch { 
				MessageBox.Show("No final picture", "error");
			}
			Text = "Pacman";
			#region /* Ikonka */
			try 
			{
				Icon = new Icon(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.pac.ico"));
			} 
			catch (Exception e) 
			{ 
				MessageBox.Show("The file could not be read:"+e.Message.ToString(), "Error with map",
				MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
			#endregion

			MyMymenu = new AppMenu(NewGame, Pause, SpeedCH, ChoseMap, ResizeField);
			MyMymenu.Parent = this;
			Controls.Add(MyMymenu);

			this.DoubleBuffered = true;

			Paint += new PaintEventHandler( this.OnStart );

			ClientSize = new Size(800, 600);	
		}	

		private void ResizeField(object sender, EventArgs e) {
			if(this.sizeField == 30) this.sizeField = 40;
			else this.sizeField = 30;
		}

		private void PrepareGame(int levelIN, int scoreIN, int livesIN)
		{

			if( this.newMap != null ) {
				this.mapa = this.newMap;
			} else { 
				this.mapa = new Map ( 0 ); 
			}

			if(this.pac == null )	this.pac = new Pacman (this.mapa , 1, 3, 0);
			else
			{
				this.pac.mapa = this.mapa;
				this.pac.position = this.mapa.GetStartPosition();
			}
			if(SB != null) SB.Dispose();

			#if DEBUG
			Console.WriteLine("[OK] Map and Pacman create.");
			#endif

			#region /* rozmery */
			this.PlaygroundWidth = this.mapa.map.GetLength(0) * this.sizeField + 30;
			this.PlaygroundHeight = this.mapa.map.GetLength(1) * this.sizeField + 60;
			#endregion	

			#region /* status bar */
			SB = new StatusBar();
			SB.Parent = this;
			SB.Text = "SPEED: " + this.actualSpeed.ToString() + ";  LIVES: 3;  SCORE: 0";
			SB.Anchor = AnchorStyles.Bottom;
			SB.Dock = DockStyle.Bottom;
			SB.Font = new Font("serif", 13);
			SB.Height = 25;
			SB.Width = this.PlaygroundWidth - 5;
			SB.ForeColor = Color.AliceBlue;
			#endregion

			this.bonusIs = true;	
			this.BackColor = Color.Black;
			this.Select();		// ziskani zamereni

			ClientSize = new Size( this.PlaygroundWidth, this.PlaygroundHeight );

			Paint -= new PaintEventHandler( this.OnStart );		
			Paint += new PaintEventHandler( this.OnPaint );		
		}

		#region /* plus/minus One turn */
		private void OnPaint(object sender, PaintEventArgs e)
		{
			int marginV = 30;  // vertical
			int marginH = 15; // horizontal

			SB.Text = "GHOSTS: " + this.mapa.numGhosts.ToString() + 
				";  SPEED: " + this.actualSpeed.ToString()     + 
				";  LIVES: " + this.pac.actualLives.ToString() + 
				";  SCORE: " + this.pac.actualScore.ToString() ;	

			Graphics g = e.Graphics;

			#region /* Draw map */
			Pen whitePen = new Pen(Brushes.MediumAquamarine);
			whitePen.Width = 2;

			for(int j = 0; j < this.mapa.map.GetLength(1); j++)
				for(int i = 0; i < this.mapa.map.GetLength(0); i++)
					if(IsDraw && !mapa.map[i,j]) g.DrawRectangle(whitePen, i * this.sizeField + marginH, 
						j * this.sizeField + marginV, this.sizeField, this.sizeField ); 
					else 
					{
						if(mapa.coins[i,j]) g.DrawImage( mapa.coin , i * this.sizeField +3 + marginH, 
							j * this.sizeField +3 + marginV );
					}

			IsDraw = true;
			g.DrawLine(whitePen , mapa.gate.X     * this.sizeField + marginH, mapa.gate.Y * this.sizeField + 45, 
				(mapa.gate.X +1) * this.sizeField + marginH, mapa.gate.Y * this.sizeField + 45);

			if(bonusIs) g.DrawImage(mapa.bonusCoin, mapa.bonus.X * this.sizeField + marginH, mapa.bonus.Y * this.sizeField + marginV);
			#endregion	

			#region /* Draw figure */
			pac.DrawToMap(g, this.sizeField ,marginH , marginV);

			foreach(Ghost gh in mapa.ghosts) {
				if(gh == null) continue;
				gh.DrawToMap(g, this.sizeField , marginH, marginV);		
			}
			#endregion

			if(pause) 
			{
				g.DrawString("PAUSA", new Font("Serif", 27) , Brushes.BlanchedAlmond, this.Width /2 - 40 , this.Height /2);
				SB.Text += "  == PAUSA  ==";
			}
		}

		private void OnTick (object sender, EventArgs e)
		{
			if(!pause) {

				if(wait > 0) {wait--; return;}

				#region	/* Pacman move */
				pac.Move ();
				if(revenge)	revengeTime--;

				if(revengeTime <= 0)
				{
					revenge = false;
					foreach(Ghost g in mapa.ghosts) g.revenge = false;
				}

				if(pac.position == mapa.bonus) 
				{
					this.bonusIs = false;
					revenge = true;
					revengeTime = 45;
					foreach(Ghost g in mapa.ghosts) g.revenge = true;
				}
				#endregion

				#region	/* Colission */
				foreach (Ghost g in mapa.ghosts)
				{
					if( g == null) continue;
					if( g.wait > 0) {g.wait--;}	
					else
						if(  g.position == pac.position )
						{
							if(revenge) g.Die();
							else GameOver(false);
						}
				}	
				#endregion

				# region /* GHOSTs move */
				foreach (Ghost g in mapa.ghosts)
				{
					if(g == null) continue;
					g.MakeDecision (this.pac); 	// timto dostane smer
					g.Move ();							
				}		
				#endregion

				#region	/* Colission */
				foreach (Ghost g in mapa.ghosts)
				{
					if( g == null) continue;
					if( g.wait > 0) {g.wait--;}	
					else
						if(  g.position == pac.position )
						{
							if(revenge) g.Die();
							else GameOver(false);
						}
				}					
				#endregion

				#region	/* Eat coin */
				if( mapa.coins[pac.position.X , pac.position.Y ]) 
				{
					if(mapa.EatCoin(pac.position)) GameOver(true) ;
					pac.actualScore++;
				}

			}

			this.Refresh ();
			#endregion
		}

		protected void OnKeyDown (object sender, KeyEventArgs e)
		{
			int key = (int)e.KeyCode;

			try {
				if (key == (int) Keys.Left  )
					pac.direction = Direction.left;
				if (key == (int) Keys.Right )
					pac.direction = Direction.right;
				if (key == (int) Keys.Up    )
					pac.direction = Direction.up;
				if (key == (int) Keys.Down  )
					pac.direction = Direction.down;
				if (key == (int) Keys.Pause )  Pause(this, null);
			} catch (Exception ex) {
				Console.WriteLine ("Chyba klavesy:\n{0}", ex.ToString ());
			}
		}
		#endregion

		#region /* "Menu" functions */

		public void SpeedCH(object sender, EventArgs e)
		{
			SpeedChange sch = new SpeedChange(this);
			sch.ShowDialog();
			sch.Dispose();
		}

		public void NewGame (object sender, EventArgs e)
		{
			StopGame();
			try{
				Paint -= new PaintEventHandler( this.OnWin );
				Paint -= new PaintEventHandler ( this.OnOver ); 
			}
			catch {}
			PrepareGame(1,0,3);

			try{
				KeyDown += new KeyEventHandler (OnKeyDown);
			}
			catch (Exception ex)
			{Console.WriteLine("{0}",ex);}

			this.pac.actualLevel = 1;
			this.pac.actualLives =3;
			this.pac.actualScore =0;

			pause = false;
			#region /* Timer */
			timer = new Timer (this.components);
			timer.Enabled = true;
			timer.Interval = (int) this.actualSpeed;
			timer.Tick += new System.EventHandler (this.OnTick);
			#endregion
		}

		public void StopGame()
		{
			this.pause = false;
			if(this.timer != null) this.timer.Dispose();
		}

		public void Pause(object sender, EventArgs e)
		{		
			switch( this.pause ) {
			case true:
				this.pause = false;
				break;
			case false:
				this.wait = 1;
				this.pause = true;
				break;
			}

		}

		public void ChoseMap(object sender, EventArgs e)
		{ 
			pause = true;

			OpenFileDialog vyber = new OpenFileDialog();
			vyber.Multiselect = false;
			vyber.Title = "Chose map";

			vyber.ShowDialog(this);
			;
			try {
				if( vyber.CheckFileExists && vyber.CheckPathExists) 
				{
					Console.WriteLine("[OK] New map: {0}", vyber.FileName);

					StopGame();	
					this.newMap = new Map( 0 );

				}
				else 
				{
					StopGame();
					PrepareGame(1 , 0 , 3);
					MessageBox.Show("Cannot open file.", "Error",
						MessageBoxButtons.OK, MessageBoxIcon.Error);
				}
			} catch{
				MessageBox.Show("Cannot open file.", "Error",
					MessageBoxButtons.OK, MessageBoxIcon.Error);
			} finally {
				vyber.Dispose();
			}
		}

		public void OnOver (object sender, PaintEventArgs e) 
		{
			timer.Stop();
			Graphics g = e.Graphics;
			g.DrawImage( this.gameover, (this.Size.Width / 2 - this.gamewin.Width / 2) , this.Size.Height /2 - this.gamewin.Height /2);  	
		}

		public void OnStart (object sender, PaintEventArgs e) 
		{
			Graphics g = e.Graphics;

			this.BackColor = Color.Black;

			Bitmap logo = ResourceManager.getLogo();
			Bitmap logoG = ResourceManager.getLogoG();
			g.DrawImage(logo, (this.ClientSize.Width / 2) - (logo.Width /2) , 45);
			g.DrawImage(logoG, 30, this.ClientSize.Height - logoG.Height - 40);
		}

		public void OnWin (object sender, PaintEventArgs e) 
		{
			timer.Stop();			
			Graphics g = e.Graphics;
			g.DrawImage( this.gamewin, (this.Size.Width / 2 - this.gamewin.Width / 2) , this.Size.Height /2 - this.gamewin.Height /2);
		}

		public void GameOver (bool bol)
		{
			switch(bol)
			{
			case true:
				Paint -= new PaintEventHandler( this.OnPaint );	
				Paint += new PaintEventHandler( this.OnWin );
				StopGame();
				break;
			case false:
				pac.actualLives--;
				pac.position = mapa.GetStartPosition();
				this.wait = 5;
				if(pac.actualLives == 0) 
				{	
					Paint += new PaintEventHandler ( this.OnOver ); 
					Paint -= new PaintEventHandler( this.OnPaint );	
					StopGame();
				}
				break;
			}
		}
		#endregion
	}
}

