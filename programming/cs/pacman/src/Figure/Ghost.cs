using System;
using System.Drawing;
using System.Windows.Forms;

namespace pacman
{
	public class Ghost : Figure
	{
		public Bitmap ghost;
		public Bitmap ghostR;
		public bool revenge;
		public int wait;
		private BaseAI ai;

		public Ghost (Map m, string character, Bitmap portret)
		{
			switch( character )
			{
			case "base" :
				this.ai = new BaseAI();
				break;
			case "guard" :
				this.ai = new GuardAI();
				break;
			case "hunter" :
				this.ai = new HunterAI();
				break;
			default :
				this.ai = new BaseAI();
				break;
			}

			this.position = m.GetStartGPosition();
			this.direction = Direction.down;
			this.mapa = m;
			this.ghost = portret;
			try
			{
				this.ghostR = ResourceManager.getGhost(4);
			} catch {
				MessageBox.Show("The ghost reverse image could not be read:", "Error",
					MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		public override void DrawToMap(Graphics g, int sizeField, int marginH, int marginV)
		{
			if( this.wait > 0) return;
			if( this.revenge)
				g.DrawImage( this.ghostR, this.position.X * sizeField + marginH, 
					this.position.Y * sizeField + marginV);
			else
				g.DrawImage(this.ghost, this.position.X * sizeField + marginH, 
					this.position.Y * sizeField + marginV);
		}

		public void MakeDecision( Figure p )
		{
			this.direction = this.ai.MakeDecision(this, p.position, this.mapa );
		}

		public void Die()
		{
			this.wait = 12;
			this.position = mapa.GetStartGPosition();
		}
	}
}

