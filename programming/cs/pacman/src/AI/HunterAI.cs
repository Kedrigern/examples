using System;
using System.Drawing;

namespace pacman
{
	public class HunterAI : BaseAI
	{
		public HunterAI() : base()
		{
		}

		override public Direction MakeDecision(Ghost g, Point pacPoint, Map map)
		{
			this.ways = g.mapa.PosibleWay( g.position ); 		// Bool array of posible way
			this.rnd = new Random();

			if( rnd.Next(1,9) == 5) return ((Direction) rnd.Next(0,3));  // Random element

			bool pravda = true;
			switch( this.ways.free )
			{
			case 1:				/* Turn round */
				if(pravda) return Reverse(g.direction);
				break;
			case 2: 			/* go straight */
				if(pravda) return TwoWays(g, ways, pacPoint);
				break;				
			case 3: 			/* prefer 2 ways */	
				if (pravda) return ThreeWays(g, ways, pacPoint);
				break;
			case 4: 			/* totaly random */	
				if(pravda) return FourWays(g, pacPoint);
				break;
			default :
				return ((Direction) rnd.Next(0,3));   
			}

			return (Direction) rnd.Next(0,3);
		}

		protected Direction TwoWays (Ghost g, Ways w, Point pacPoint)
		{
			Direction first = Direction.down;
			Direction second = Direction.up;
			bool was = false;
			for(int i = 0; i <=3;i++)
				if(w.ways[i]) {
					if(!was) { first = (Direction) i; was =true; }
					else second = ((Direction) i);
				}

			if(1 == PacmanNear( Figure.Shift(first, g.position), Figure.Shift(second, g.position), pacPoint)) return (Direction) first;
			else return (Direction) second;
		}

		protected Direction ThreeWays (Ghost g, Ways w, Point pacPoint)
		{
			Direction secondary;
			Direction primary1 = Direction.up;
			Direction primary2 = Direction.down;
			bool was = false;
			byte decision;

			secondary = Reverse(g.direction);
			w.ways[(int) secondary] = false;

			for(int i = 0; i <=3;i++)
			{
				if(w.ways[i]) {
					if(!was) { primary1 = ((Direction) i); was =true; }
					else primary2 = ((Direction) i);
				}
			}

			if(rnd.Next(0,9) == 4) decision = (byte) rnd.Next(1,3);
			else
				if(rnd.Next(0,5) == 2) decision = PacmanNear( Figure.Shift(primary1 , g.position), Figure.Shift( primary2 , g.position ), Figure.Shift(secondary, g.position), pacPoint);
				else decision = PacmanNear( Figure.Shift(primary1,g.position), Figure.Shift( primary2, g.position ), pacPoint);

			if(decision == 1) return primary1;
			if(decision == 2) return primary2;
			return secondary;
		} 

		protected Direction FourWays (Ghost g, Point pacPoint)
		{
			return (Direction) PacmanNear( Figure.Shift(Direction.up, g.position), 
				Figure.Shift(Direction.down, g.position), 
				Figure.Shift(Direction.left, g.position), 
				Figure.Shift(Direction.right, g.position), pacPoint);
		}	
	}
}