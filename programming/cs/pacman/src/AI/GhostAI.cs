using System;
using System.Drawing;

namespace pacman
{
	public interface GhostAI
	{
		Direction MakeDecision(Ghost g, Point pacPoint, Map map );
	}
}