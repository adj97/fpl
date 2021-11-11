using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FplAnalysis.ReturnClasses
{
    class TopElement
    {
        public TopElement(dynamic json)
        {
            Id = json.id;
            Points = json.points;
        }

        public int Id { get; set; }
        public int Points { get; set; }
    }
}
