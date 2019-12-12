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
            var lines = File.ReadAllLines("Sample.txt");
            var route1 = BuildLines(lines[0].Split(','));
            var route2 = BuildLines(lines[1].Split(','));

            var intersections = new List<(int x, int y)>();
            var distances = new List<int>();
            foreach (var line in route1)
            {
                foreach (var line2 in route2)
                {
                    if (line.DoLinesCross(line2, out var intersection, out var distanceTravelled))
                    {
                        intersections.Add(intersection);
                        distances.Add(distanceTravelled);
                    }
                }
            }

            var part1 = intersections
                                .Select(pt => Math.Abs(pt.x) + Math.Abs(pt.y))
                                .OrderBy(d => d)
                                .First();

            var part2 = distances.Min();
        }

        private static List<Line> BuildLines(string[] moves)
        {
            var lines = new List<Line>();
            var totalDistance = 0;
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

                lines.Add(new Line(totalDistance, point, newPoint));

                point = newPoint;
                totalDistance += distance;
            }

            return lines;
        }
    }
}
