using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day3
{
    class Program
    {
        static void Main()
        {
            var lines = File.ReadAllLines("Part1.txt");
            var route1 = BuildLines(lines[0].Split(','));
            var route2 = BuildLines(lines[1].Split(','));

            var intersections = new List<(int x, int y)>();
            foreach (var line in route1)
            {
                foreach (var line2 in route2)
                {
                    if (line.DoLinesCross(line2, out var intersection))
                    {
                        intersections.Add(intersection);
                    }
                }
            }

            var distances = intersections
                                .Select(pt => Math.Abs(pt.x) + Math.Abs(pt.y))
                                .OrderBy(d => d);
        }

        private static List<Line> BuildLines(string[] moves)
        {
            var lines = new List<Line>();

            (int x, int y) point = (0, 0);
            foreach (var move in moves)
            {
                var direction = move[0];
                var distance = int.Parse(move.Substring(1));

                var newPoint = direction switch
                {
                    'R' => (point.x + distance, point.y),
                    'L' => (point.x - distance, point.y),
                    'U' => (point.x, point.y + distance),
                    _ => (point.x, point.y - distance),
                };

                lines.Add(new Line(point, newPoint));

                point = newPoint;
            }

            return lines;
        }
    }
}
