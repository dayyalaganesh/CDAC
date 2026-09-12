"""
Scenario: You are organizing a movie marathon. You start with a playlist:["Inception", "TheMatrix", "Interstellar"].
Prompt the use to enter the name of a movie they want to add.
If the movie is already in the list ,print"Already added!"and do not insert it.
If it is not in the list, append it to the end of the list.
Finally, sort the movie list alphabetically and print the updated playlist.
SampleInput:"Interstellar"
SampleOutput
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']

SampleInput:"Avatar"
SampleOutput:
Added Avatar!
Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'TheMatrix']
"""
def main():
    playlist=["Inception", "TheMatrix", "Interstellar"]
    mname=input("Enter any movie name: ").capitalize()
    if mname in playlist:
        print("Already added! and do not insert")
    else:
        playlist.append(mname)
        playlist.sort()
        print(playlist)
main()