using System;
using System.Drawing;
using System.IO;

namespace pacman
{
	public static class ResourceManager
	{
		public static Bitmap getLogo() {
			return new Bitmap( System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.logo.png"));
		}

		public static Bitmap getLogoG() {
			return new Bitmap( System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.logoG.png"));
		}

		public static Bitmap getGhost(byte type = 1) {
			switch(type) {
			case 1:
				return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.ghost.png"));
			case 2:
				return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.ghost.red.png"));
			case 3:
				return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.ghost.green.png"));
			case 4:
			default:
				return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.ghostR.png"));
			}
		}

		public static Bitmap getCoin(byte type = 1) {
			switch(type) {
			case 1:
				return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.coin.png"));
			case 2:
			default:
				return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.coin2.png"));
			}
		}

		public static Bitmap getPacman() {
			return new Bitmap(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.player.png"));
		}

		public static Stream getMap() {
			return System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream( "pacman.Resources.map-general.txt");
		}

		/* Alternativly we can download from internet:
		Console.WriteLine("Missing graphic - Maybe I can download");
		WebRequest wReq = WebRequest.Create("http://example.org//player.png");  // using System.Net;
		WebResponse wRes = wReq.GetResponse();
		Stream strm = wRes.GetResponseStream();	
		this.player = (Bitmap) Image.FromStream(strm);
		Console.WriteLine("OK, I have the graphic, that miss.");
		*/
	}
}

