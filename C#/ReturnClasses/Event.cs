using System;
using FplAnalysis.Helper;

namespace FplAnalysis.ReturnClasses
{
    class Event
    {
        public Event(dynamic json)
        {
            Id = json.id;
            Name = json.name;
            DeadlineTime = json.deadline_time;
            AverageEntryScore = json.average_entry_score;
            Finished = json.finished;
            DataChecked = json.data_checked;
            HighestScoringEntry = json.highest_scoring_entry;
            DeadlineTimeEpoch = json.deadline_time_epoch;
            DeadlineTimeGameOffset = json.deadline_time_game_offset;
            HighestScore = json.highest_score;
            IsPrevious = json.is_previous;
            IsCurrent = json.is_current;
            IsNext = json.is_next;
            MostSelected = json.most_selected;
            MostTransferredIn = json.most_transferred_in;
            TransfersMade = json.transfers_made;
            MostCaptained = json.most_captained;
            MostViceCaptained = json.most_vice_captained;

            TopElement = new TopElement(json.top_element_info);

            foreach (dynamic chip in json.chip_plays)
            {
                if (chip.chip_name == "bboost")
                {
                    BenchBoost = chip.num_played;
                }
                if (chip.chip_name == "freehit")
                {
                    FreeHit = chip.num_played;
                }
                if (chip.chip_name == "wildcard")
                {
                    WildCard = chip.num_played;
                }
                if (chip.chip_name == "3xc")
                {
                    TripleCaptain = chip.num_played;
                }
            }
        }

        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime DeadlineTime { get; set; }
        public int AverageEntryScore { get; set; }
        public bool Finished { get; set; }
        public bool DataChecked { get; set; }
        public int HighestScoringEntry { get; set; }
        public int DeadlineTimeEpoch { get; set; }
        public int DeadlineTimeGameOffset { get; set; }
        public int HighestScore { get; set; }
        public bool IsPrevious { get; set; }
        public bool IsCurrent { get; set; }
        public bool IsNext { get; set; }
        public int MostSelected { get; set; }
        public int MostTransferredIn { get; set; }
        public int TransfersMade { get; set; }
        public int MostCaptained { get; set; }
        public int MostViceCaptained { get; set; }
        public TopElement TopElement { get; set; }
        public int BenchBoost { get; set; }
        public int FreeHit { get; set; }
        public int TripleCaptain { get; set; }
        public int WildCard { get; set; }
    }
}
