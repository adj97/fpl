using System.Collections.Generic;

namespace FplAnalysis.ReturnClasses
{
    class Model
    {
        public Model(dynamic json)
        {
            Settings = new GameSettings(json);
            TotalFplPlayers = json.total_players;

            Events = new List<Event>();
            foreach(var eventObj in json.events)
            {
                Events.Add(new Event(eventObj));
            }
            Phases = new List<Phase>();
            Teams = new List<Team>();
            Players = new List<Player>();
            PlayerStats = new List<PlayerStat>();
            PlayerType = new List<PlayerType>();

        }

        public List<Event> Events { get; set; }

        public GameSettings Settings { get; set; }

        public List<Phase> Phases { get; set; }

        public List<Team> Teams { get; set; }

        public List<Player> Players { get; set; }

        public List<PlayerStat> PlayerStats { get; set; }

        public List<PlayerType> PlayerType { get; set; }

        public int TotalFplPlayers { get; set; }
    }
}
