# FPL API Data Analysis and AI
Initially written in C#, converting to python

~~Use `git add --all -- ':!C#/*'` to ignore all the c# stuff~~

I've actually added `Cs/*` to the gitignore, so actually comment that out if you want to contribute C# code

## API Reference
This is a good guide for the FPL API [medium.com](https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19)

#### Public Endpoints
 - https://fantasy.premierleague.com/api/bootstrap-static/
 - https://fantasy.premierleague.com/api/fixtures/
 - https://fantasy.premierleague.com/api/element-summary/{element_id}/
 - https://fantasy.premierleague.com/api/event/{event_id}/live/
 - https://fantasy.premierleague.com/api/entry/{manager_id}/
 - https://fantasy.premierleague.com/api/entry/{manager_id}/history/
 - https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings
 - https://fantasy.premierleague.com/api/entry/{manager_id}/event/{event_id}/picks/
 - https://fantasy.premierleague.com/api/event-status/
 - https://fantasy.premierleague.com/api/dream-team/{event_id}/
 - https://fantasy.premierleague.com/api/team/set-piece-notes/

####  Endpoints (Auth)
 - https://fantasy.premierleague.com/api/my-team/{manager_id}/