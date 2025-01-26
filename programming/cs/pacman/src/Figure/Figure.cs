using System;
using System.Drawing;

namespace pacman
{
	public abstract class Figure
	{
		public Point position;
		public Direction direction;
		public Map mapa;		

		public void ChangeDirection( Direction D )
		{
			this.direction = D;
		}

		public Point Shift()
		{
			return Shift(direction, this.position);
		}

		public static Point Shift(Direction d, Point position)
		{
			int x = 0;
			int y = 0;

			switch(d)
			{
			case Direction.up : 
				x = position.X;
				y = position.Y -1;
				break;
			case Direction.down :
				x = position.X;			
				y = position.Y+1;	
				break;
			case Direction.left :
				x = position.X-1;
				y = position.Y;
				break;
			case Direction.right :
				x = position.X+1;
				y = position.Y;
				break;
			}
			return new Point(x,y);
		}

		public void Move()
		{
			Point point = Shift();

			if( mapa.CheckIn( point ) ) this.position = point;
		}

		public virtual void DrawToMap(Graphics g, int sizeField, int marginH, int marginV)
		{
			g.DrawEllipse(Pens.Blue, (this.position.X * sizeField) + marginH +5, (this.position.Y * sizeField) + marginV+ 5, 12 , 12 );
		}
	}
}

