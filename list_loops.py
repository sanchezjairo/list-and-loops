songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])

print(songs[1:3])

songs[2] = "SICKO MODE"
print(songs)

songs.append("For the Night")
songs.extend(["Savage mode", "ASTROTHUNDER"])
print(songs)
songs.remove("Do It")
print(songs)