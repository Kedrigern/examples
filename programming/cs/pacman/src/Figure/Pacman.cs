using System;
using System.Drawing;
using System.Windows.Forms;

namespace pacman
{
	public class Pacman : Figure
	{
		public int actualLevel;
		public int actualLives;
		public int actualScore;

		private Bitmap pacmanRight;
		private Bitmap pacmanLeft;
		private Bitmap pacmanUp;
		private Bitmap pacmanDown;

		public Pacman ( pacman.Map m , int a , int b, int c)
		{
			this.actualLevel = a;
			this.actualLives = b;
			this.actualScore = c;
			this.position = m.GetStartPosition();
			this.mapa = m;
			this.direction = Direction.right;

			PacmanLoadICon ();
		}

		public override void DrawToMap(Graphics g, int sizeField, int marginH, int marginV)
		{
			switch( this.direction ) 
			{
			case Direction.right :
				g.DrawImage( this.pacmanRight , this.position.X * sizeField +3 + marginH, 
					this.position.Y * sizeField +3 + marginV); 
				break;
			case Direction.left :
				g.DrawImage( this.pacmanLeft , this.position.X * sizeField +3 + marginH, 
					this.position.Y * sizeField +3 + marginV);
				break;
			case Direction.down : 				
				g.DrawImage( this.pacmanDown , this.position.X * sizeField +3 + marginH, 
					this.position.Y * sizeField +3 + marginV);
				break;
			case Direction.up :
				g.DrawImage( this.pacmanUp , this.position.X * sizeField +3 + marginH,
					this.position.Y * sizeField +3 + marginV);
				break;
			}
		}

		private void PacmanLoadICon()
		{
			try {
				Bitmap pacman = ResourceManager.getPacman();
				this.pacmanRight = (Bitmap) pacman.Clone();
				this.pacmanLeft = (Bitmap) pacman.Clone();
				this.pacmanDown = (Bitmap) pacman.Clone();
				this.pacmanUp = (Bitmap) pacman.Clone();

				this.pacmanLeft.RotateFlip( RotateFlipType.RotateNoneFlipX );
				this.pacmanDown.RotateFlip( RotateFlipType.Rotate90FlipNone  );
				this.pacmanUp.RotateFlip( RotateFlipType.Rotate90FlipXY );
			}
			catch (Exception e)
			{
				MessageBox.Show("The file could not be read:"+e.Message.ToString(), "Error with map",
					MessageBoxButtons.OK, MessageBoxIcon.Error);				
			}
		}	
	}
}