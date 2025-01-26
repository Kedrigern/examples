using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace pacman
{
	public class Map
	{
		private int numCoins;
		public int numGhosts;
		public bool[,] map;
		public bool[,] coins;
		public Bitmap coin;
		public Bitmap bonusCoin;
		public List< pacman.Ghost > ghosts;
		private Point start;		// Pacman start field
		private Point gstart;		// Ghosts start field
		public Point gate;
		public Point bonus;

		#region /* Constructors */	
		public Map (int numberOfGhosts, string path = null)
		{			
			int sizeV = 1;
			int sizeH = 0;

			try {
				StreamReader sr;
				if(path == null) {
					sr = new StreamReader(ResourceManager.getMap());
				} else{
					sr = new StreamReader (path);
				}
				using ( sr ) 
				{
					string line = sr.ReadLine();
					sizeH = line.Length;
					while(sr.ReadLine() != null) sizeV++;
				} 
			} catch (Exception e) {
				MessageBox.Show(
					"Cannot find map definition.", 
					"Error",
					MessageBoxButtons.OK, 
					MessageBoxIcon.Error
				);
			}

			try { 	
				this.coin = ResourceManager.getCoin();
				this.bonusCoin = ResourceManager.getCoin(2);
			} catch (Exception e) {
				MessageBox.Show(
					"Cannot find coin's picture." + e.Message , 
					"Error",
					MessageBoxButtons.OK, 
					MessageBoxIcon.Error
				);
			}

			map = new bool[sizeH, sizeV];
			coins = new bool[sizeH, sizeV];
			LoadFromFile (path);
			SetCoins();

			if(numberOfGhosts != 0 ) {CreateGhosts (numberOfGhosts); this.numGhosts = numberOfGhosts;}
			if((sizeH * sizeV) < 200 ) {CreateGhosts (1); this.numGhosts = 1; return;}
			if((sizeH * sizeV) < 300 ) {CreateGhosts (2); this.numGhosts = 2; return;}
			if((sizeH * sizeV) < 450 ) {CreateGhosts (3); this.numGhosts = 3; return;}
			if((sizeH * sizeV) < 550 ) {CreateGhosts (4); this.numGhosts = 4; return;}
			if((sizeH * sizeV) < 700 ) {CreateGhosts (5); this.numGhosts = 5; return;}
			if((sizeH * sizeV) < 900 ) {CreateGhosts (6); this.numGhosts = 6; return;}
			if((sizeH * sizeV) > 999 ) {CreateGhosts (7); this.numGhosts = 7; return;}	
		}	

		private void CreateGhosts (int numberOfGhosts)
		{
			try {
				Bitmap ghostWhite = ResourceManager.getGhost();
				Bitmap ghostRed  = ResourceManager.getGhost(2); 
				Bitmap ghostGreen  =  ResourceManager.getGhost(3);

				this.ghosts = new List<Ghost> (numberOfGhosts);
				for (int i = 1; i <= numberOfGhosts; i++)
				{
					if(i ==1) this.ghosts.Add(new Ghost(this, "hunter", ghostRed));
					else {
						if(i % 2 == 0) this.ghosts.Add(new Ghost(this, "base", ghostWhite));
						else this.ghosts.Add(new Ghost(this, "guard", ghostGreen));
					}
				}
			}
			catch {
				MessageBox.Show("Cannot find ghost's picture.", "Error",
					MessageBoxButtons.OK, MessageBoxIcon.Error); }
		}

		private void SetCoins()
		{
			numCoins = 0;
			for(int j = 0; j< map.GetLongLength(1); j++)
				for(int i = 0; i < map.GetLongLength(0); i++)
					if(map[i,j]) 
					{
						coins[i,j] = true;
						numCoins++;
					}
					else coins[i,j] = false;

			coins[start.X  , start.Y ] = false;
			coins[gstart.X , gstart.Y] = false;
			coins[gate.X   , gate.Y  ] = false;
			coins[bonus.X  , bonus.Y ] = false;
			numCoins -= 4;
		}

		public bool EatCoin(Point p)
		{
			coins[ p.X , p.Y ] = false;
			numCoins--;
			if(numCoins < 1) return true;
			else return false;
		}

		private void LoadFromFile (string path)
		{
			try 
			{
				StreamReader sr;
				if(path == null) {
					sr = new StreamReader(ResourceManager.getMap());
				} else{
					sr = new StreamReader (path);
				}
				using (sr) 
				{
					int j = 0;
					String line;
					while ((line = sr.ReadLine ()) != null) 
					{

						for (int i = 0; i < line.Length; i++)
							switch (line[i]) {
						case 'X':
							map[i, j] = false;
							break;
						case '.':
							map[i, j] = true;
							break;
						case 'S':
						case 's':
							map[i, j] = true;
							start = new Point (i, j);
							break;
						case 'G':
						case 'g':
							map[i, j] = true;
							gstart = new Point (i, j);
							break;
						case '_':
						case '|':
							map[i,j] = true;
							this.gate = new Point(i,j);
							break;
						case 'C':
							map[i,j] = true;
							this.bonus = new Point(i,j);
							break;
						default  : map[i, j] = true;  break;
						}
						j++;
					}
				}
			}
			catch (Exception e) 
			{
				MessageBox.Show("The file could not be read:"+e.Message.ToString(), "Error with map",
					MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}
		#endregion

		public Point GetStartPosition ()
		{
			return start; 
		}

		public Point GetStartGPosition ()
		{
			return gstart;
		}

		public bool CheckIn(Point p)
		{
			return CheckIn(p.X , p.Y);
		}

		public bool CheckIn(int a , int b)
		{	/* This procedure compute in unit metric, only graphics is mull by sizeOfSquere */
			if ( (a >= 0) &&
				(a <= map.GetLength(0) ) &&
				(b >= 0) &&
				(b <= map.GetLength(1) ) &&
				map[a,b] )
				return true;
			else return false;
		}

		public Ways PosibleWay(Point p)
		{
			return PosibleWay(p.X , p.Y);
		}

		public Ways PosibleWay(int a, int b)
		{
			Ways w = new Ways(); 		// inicialization to false
			w.free = 0;
			w.ways = new bool[4];
			for(int i = 0; i<4; i++) w.ways[i] = false;

			if(CheckIn(a, b-1)) { w.ways[(int) Direction.up  ] = true; w.free++; } 
			if(CheckIn(a, b+1)) { w.ways[(int) Direction.down] = true; w.free++; } 
			if(CheckIn(a-1, b))	{ w.ways[(int) Direction.left] = true; w.free++; } 
			if(CheckIn(a+1, b)) { w.ways[(int) Direction.right] = true; w.free++; }	// right
			return w;
		}

		public override string ToString()
		{
			string outs = ""; 

			for(int j = 0; j < map.GetLength(1); j++)
			{ 	for(int i = 0; i < map.GetLength(0); i++)
				{
					if(map[i,j]) outs += '.';
					else outs += 'X';
				}
				outs += '\n';
			}	
			return outs;
		}
	}
}

