#3-9 Dinner Guest (use len() to print number if invited guest)

#3-4 Guest List

guest = ['Bob Barker', "Bill O Riely", "Tommy Pickles"]
invitation = f'{guest[0]},\n \t Your cordially invited to MY dinner party & should be honored to be invited.'
print(invitation)
invitation = f'{guest[1]},\n \t Your cordially invited to MY dinner party & should be honored to be invited.'
print(invitation)
invitation = f'{guest[2]},\n \t Your cordially invited to MY dinner party & should be honored to be invited.'
print(invitation)
print(len(guest))
#3-5 Changing Guest List
uninvited = guest.pop(1)
guest.append('Kali Uchi')
print(uninvited +" made some racist comments so we had to take back our invitatioin")
print(f'So now our guest list includes {guest[0]}, {guest[1]}. & {guest[2]}')
print(len(guest))

#3-6 More Guest

guest.insert(0,'Derek Sperick')
guest.insert(3,"Dirty Mike")
guest.append("Piss Ant")

print("My neighbor was throwing out this real nice bigger table then what I currently have, so now we have some more space")
print(f"Now our guest list consist of  {guest[0]}, {guest[1]}. {guest[2]}, {guest[3]}, {guest[4]} & {guest[5]}")
print(len(guest))

#3-7 Shrinking Guest List
print("So the table was infested with termites & I already threw out my old table. We can eat on my couch but then I can only invite like 2 people.")
sorrybruh = guest.pop()
print(f'sorry {sorrybruh} but your out')
sorrybruh = guest.pop()
print(f'sorry {sorrybruh} but your out')
sorrybruh = guest.pop()
print(f'sorry {sorrybruh} but your out')
sorrybruh = guest.pop()
print(f'sorry {sorrybruh} but your out')

print(f"So, I've decided to invite you, {guest[0]} & {guest[1]} cause your my very special guest & I could never forget you two")
del guest[1]
del guest[0]
print(guest)
print(len(guest))
