using System;

namespace Day3
{
    internal class Line
    {
        private (int x, int y) point1;
        private (int x, int y) point2;

        private (int x, int y) _startPoint;

        private int _distanceToStartOfLine;

        public Line(int distanceToStartOfLine, (int x, int y) point1, (int x, int y) point2)
        {
            _distanceToStartOfLine = distanceToStartOfLine;
            _startPoint = point1;
            this.point1 = (Math.Min(point1.x, point2.x), Math.Min(point1.y, point2.y));
            this.point2 = (Math.Max(point1.x, point2.x), Math.Max(point1.y, point2.y));
        }

        public bool IsVertical => point1.x == point2.x;
        public bool IsHorizontal => point1.y == point2.y;

        public bool DoLinesCross(Line otherLine, out (int x, int y) point, out int distanceTravelled)
        {
            distanceTravelled = 0;
            point = (0, 0);

            if (this.IsHorizontal == otherLine.IsHorizontal) return false;

            var y = this.IsHorizontal ? this.point1.y : otherLine.point1.y;
            var x = this.IsVertical ? this.point1.x : otherLine.point1.x;

            if (x >= this.point1.x && x >= otherLine.point1.x && x <= this.point2.x && x <= otherLine.point2.x &&
                y >= this.point1.y && y >= otherLine.point1.y && y <= this.point2.y && y <= otherLine.point2.y)
            {
                distanceTravelled = _distanceToStartOfLine + Math.Abs(y - _startPoint.y) + Math.Abs(x - _startPoint.x);
                point = (x, y);
                return true;
            }

            return false;
        }
    }
}