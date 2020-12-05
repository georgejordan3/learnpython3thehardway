def gear_ratio(chainring, cog):
    print(f"You have {chainring} teeth on your chainring.")
    print(f"You have {cog} teeth on your cog.")
    print(f"That's a gear ration of {chainring} \ {cog}.")
    print("That's a good ratio!")

chainring = input("How many teeth on your chainring? ")
cog = input("How many teeth on your cog? ")
gear_ratio(chainring, cog)
