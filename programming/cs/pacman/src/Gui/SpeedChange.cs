using System;
using System.Windows.Forms;
using System.Drawing;
using System.ComponentModel;

namespace pacman
{
	public class SpeedChange : Form
	{
		Label aktual;
		MainWindow game;
		Button sl;
		Button me;
		Button fa;

		public SpeedChange(MainWindow ok) : base()
		{
			this.Text = "Speed";
			this.game = ok;
			this.MaximizeBox = false;
			this.MinimizeBox = false;

			aktual = new Label();
			aktual.Parent = this;
			aktual.Text = "Aktualni rychlost: " + this.game.actualSpeed.ToString();
			aktual.Location = new Point(15,12);

			sl = new Button();
			me = new Button();
			fa = new Button();

			this.Size = new Size(175,135);

			sl.Text = "Slow";
			sl.Parent = this;
			sl.Dock = DockStyle.Bottom;
			sl.Click += new EventHandler( this.OnClick);

			me.Text = "Medium";
			me.Parent = this;
			me.Dock = DockStyle.Bottom;
			me.Click += new EventHandler( this.OnClick);

			fa.Text = "Fast";
			fa.Parent = this;
			fa.Dock = DockStyle.Bottom;					
			fa.Click += new EventHandler( this.OnClick);

			this.AcceptButton = fa;
		}

		private void OnClick(object sender, EventArgs e)
		{
			if( sender == this.sl ) 
			{ 
				Console.WriteLine("Slow ({0})", (int) Speed.slow);
				this.game.actualSpeed = pacman.Speed.slow;
				this.Close();
			}
			if( sender == this.me ) 
			{
				Console.WriteLine("Medium ({0})",(int) Speed.medium);
				this.game.actualSpeed = Speed.medium;
				this.Close();
			}
			if( sender == this.fa ) 
			{
				Console.WriteLine("Fast ({0})", (int) Speed.fast);				
				this.game.actualSpeed = Speed.fast;
				this.Close();
			}
		}
	}
}