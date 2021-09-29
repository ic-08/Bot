import discord
def events():
    embed = discord.Embed(
        title = "School Events", 
        color = 0x808080)
    #Events
    embed.add_field(name = "Events Below:", value = "\n\n**X-Running Club Day 1/3/5**\nMeet at the Outdoor Classroom in the front of the school WITH your lunch at 11-11:05am\nClub will run in the neighborhood from 11:05-11:25 and then eat lunch together in the outdoor classroom space. \nFIRST RUN on Tuesday Sept 28th \nYOU MUST HAVE YOUR WALKING FORM RETURNED TO PARTICIPATE\n\n\n**ORANGE SHIRT DAY T-SHIRT DESIGN.**\nIn 2017, Homelands hosted a design contest for Orange Shirt Day. Although the new shirt will not be ready before this year’s event, we hope to outfit interested staff and students with a new shirt that helps educate others about the significance of Orange Shirt Day. \n\n*Criteria:*\nMust include the slogan “Every Child Matters”\nCan easily be printed on an orange t-shirt\nIncludes indigenous symbols or influences (e.g. eagle, sun, medicine wheel, elements, etc.)\nCan be easily digitized (if you did it on paper, so it can be made into an electronic version)\nPlease submit your final entry to Mme Linthwaite in Room 111B or submit through this link!",  inline = False)

    embed.add_field(name = "BRAVE SPACES", value = "BRAVE SPACES\nTeachers at Homelands are meeting at the end of this week to revamp our Brave Space clubs so that they can continue during this 2nd/3rd year of a pandemic. This includes all of our equity groups, including Spectrum, Umoja, Bridges and TRC. If you would like to learn more about Brave Spaces, on your own or as a class, please check out our website. It has been updated with information about each of these clubs. As well, we are looking for input from students! If you would like to provide feedback, please complete this form (also sent to you via email)Thank you\nWebsite : https://sites.google.com/pdsb.net/brave/home\nForm : https://sites.google.com/pdsb.net/brave/home")
    
    embed.set_footer(text="Written with Python.")
    return embed
