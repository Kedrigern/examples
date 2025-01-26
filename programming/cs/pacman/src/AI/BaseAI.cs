using System;
using System.Drawing;

namespace pacman
{
	public class BaseAI : GhostAI
	{
		protected Random rnd; 
		protected Ways ways;

		public virtual Direction MakeDecision(Ghost g, Point pacPoint, Map map)
		{
			this.ways = g.mapa.PosibleWay( g.position ); 		// Bool array of posible way
			this.rnd = new Random();

			if( rnd.Next(1,9) == 5) return ((Direction) rnd.Next(0,4));  // Random element

			bool pravda = true;
			switch( this.ways.free )
			{
			case 1:				/* Turn round */
				if(pravda) return OneWay(g);
				break;
			case 2: 			/* go straight */
				if(pravda) return TwoWays(g);
				break;				
			case 3: 			/* prefer 2 ways */	
				if (pravda) return ThreeWays(g, this.ways);
				break;
			case 4: 			/* totaly random */	
				if(pravda) return FourWays(g.direction);
				break;
			default :
				return ((Direction) rnd.Next(0,4));   
			}

			return (Direction) rnd.Next(0,3);
		}

		protected virtual Direction OneWay(Ghost g)
		{
			return Reverse( g.direction );	
		}

		protected virtual Direction TwoWays(Ghost g)
		{
			foreach(Ghost ga in g.mapa.ghosts)
				if( g.Shift() == ga.position ) return DecisionTurn(g);

			if( g.mapa.CheckIn( g.Shift() )) return g.direction;
			else return DecisionTurn(g);
		}

		protected virtual Direction ThreeWays(Ghost g, Ways w )
		{
			Direction secondary;
			Direction primary1 = Direction.up;
			Direction primary2 = Direction.down;
			bool was = false;

			secondary = Reverse(g.direction);

			for(int i = 0; i <=3;i++)
				if(w.ways[i]) {
					if(!was) { primary1 = (Direction) i; was =true; }
					else primary2 = ((Direction) i);
				}

			switch(rnd.Next(0,7))
			{
			case 0:
			case 2:
			case 4:
				return primary1;
				break;
			case 1:
			case 3:
			case 5:
				return primary2;
				break;
			default :
				return secondary;
				break;
			}			
		}

		protected virtual Direction FourWays(Direction d)
		{
			Direction ret = d;
			while(d == ret) ret = (Direction) rnd.Next(0,3);
			return ret;
		}

		protected virtual Direction DecisionTurn(Ghost g)
		{
			switch(g.direction)
			{
			case Direction.up :
			case Direction.down :
				if( ways.ways[ 3 ] ) return Direction.right;
				if( ways.ways[ 2 ] ) return Direction.left;
				break;
			case Direction.left:
			case Direction.right:
				if( ways.ways[0] ) return Direction.up;
				if( ways.ways[1] ) return Direction.down;
				break;
			}
			return Direction.right;
		}

		protected static Direction Reverse(Direction d)
		{
			bool pravda = true;
			switch(d)// HACK: problem with warnigs and compilater if I put return in case...
			{
			case Direction.up :
				if(pravda) return Direction.down; 
				break;
			case Direction.down :
				if(pravda) return Direction.up; 
				break;
			case Direction.left :
				if(pravda) return Direction.right; 
				break;
			case Direction.right:
				if(pravda) return Direction.left; 
				break;
			default : 
				if(pravda) return Direction.up; 
				break;
			}
			return Direction.up;	// HACK:
		}

		protected static byte PacmanNear(Point first, Point second, Point pac)
		{
			return PacmanNear(first, second, new Point(1500,1500), pac);
		}

		protected static byte PacmanNear(Point first, Point second, Point third, Point pac)
		{
			int f = Math.Abs( first.X - pac.X ) + Math.Abs( first.Y - pac.Y);
			int s = Math.Abs( second.X - pac.X) + Math.Abs( second.Y - pac.Y);
			int t = Math.Abs( third.X - pac.X ) + Math.Abs( third.Y - pac.Y ); 

			int min = Math.Min(f , Math.Min(s,t)  );

			if(min == f) return 1;
			if(min == s) return 2;
			if(min == t) return 3;
			return 2;
		}

		protected static byte PacmanNear(Point fir, Point sec, Point thi, Point fou, Point pac)
		{
			int fi = Math.Abs( fir.X - pac.X ) + Math.Abs( fir.Y - pac.Y);
			int se = Math.Abs( sec.X - pac.X ) + Math.Abs( sec.Y - pac.Y);
			int th = Math.Abs( thi.X - pac.X ) + Math.Abs( thi.Y - pac.Y );
			int fo = Math.Abs( fou.X - pac.X ) + Math.Abs( fou.X - pac.Y );
			int min = Math.Min( Math.Min(fi, se) , Math.Min(th,fo) );

			/*  UNDONE: Two same-score way */
			if(min == fi) return 0;
			if(min == se) return 1;
			if(min == th) return 2;
			if(min == fo) return 3;
			return 3;
		}

		protected bool[] Coin(Point here, Map map)
		{
			bool[] co = new bool[5];
			for(int i = 0; i < 4; i++)
				if( map.coins[ Figure.Shift( (Direction) i , here).X , Figure.Shift( (Direction) i , here).Y ] ) co[i] = true;
				else co[i] = false;

			co[4] = false;

			return co;
		}
	}
}