#i
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(len(justice_league))
print(justice_league)

#ii
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

#iii
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)

#iv
justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print(justice_league)

#v
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)

#vi
justice_league.sort()
print(justice_league)
print(justice_league[0])

