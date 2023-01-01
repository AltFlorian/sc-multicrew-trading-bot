import re

users = []
investments = []
expenses = []
expensesDescription = []
revenues = []
revenuesDescription = []

userPattern = re.compile(r"!adduser [a-zA-Z]+ [0-9]+", re.IGNORECASE)
pattern = re.compile(r"![a-zA-Z]+ [0-9]+ [a-zA-Z0-9]+", re.IGNORECASE)

def check_negative(s):
    try:
        f = float(s)
        if (f < 0):
            return True
        # Otherwise return false
        return False
    except ValueError:
        return False

def get_response(message) -> str:
    message = message.lower()
    if '!adduser' in message:
        if userPattern.match(message):
            content = message.split()
            users.append(content[1])
            investments.append(int(float(content[2])))
            return f'👤User {content[1]} with a investment of {content[2]} aUEC added.'
        else:
            return '❗Incorrect pattern to add a user. \nType "!adduser <name> <amount of aUEC invested>" or "!help" ' \
                   'for all available commands.'

    if message == '!start' or message == '!restart':
        users.clear()
        investments.clear()
        expenses.clear()
        expensesDescription.clear()
        revenues.clear()
        revenuesDescription.clear()
        return '**🔥🔥🔥🔥   Everything cleared.   🔥🔥🔥🔥** \n```Type "!help" for all available commands. ```'

    if '!minus' in message:
        if pattern.match(message):
            content = message.split()
            expenses.append(int(float(content[1])))
            expensesDescription.append(content[2])
            return f'🟥Expense for {content[2]} of {content[1]} aUEC added.'
        else:
            return '❗Incorrect pattern to add a expense.\nType "!minus <amount of aUEC> <expense description>" or ' \
                   '"!help" for all available commands.'

    if '!plus' in message:
        if pattern.match(message):
            content = message.split()
            revenues.append(int(float(content[1])))
            revenuesDescription.append(content[2])
            return f'🟩Revenue for {content[2]} of {content[1]} aUEC added.'
        else:
            return '❗Incorrect pattern to add a revenue.\nType "!plus <amount of aUEC> <revenue description>" or ' \
                   '"!help" for all available commands.'

    if message == '!sum':
        try:
            sum = 0
            investmentsSum = 0
            for i in investments:
                investmentsSum = investmentsSum + i
                sum = sum + i
            for x in expenses:
                sum = sum - x
            for y in revenues:
                sum = sum + y
            portion = sum / len(users)
        except:
            return '❗️Sum could not be calculated. Please add expenses and incomes.'
        try:
            percentageStr = '\n**⚖️ Percentage breakdown:**\n'
            for index, z in enumerate(users):
                percentage = int(float(investments[index])) / investmentsSum
                percentageMoney = sum * percentage
                percentageStr = percentageStr + f'    👤{z} gets {int(float(percentageMoney))} aUEC.\n'

            if check_negative(sum):
                return f'🏆 **Total loss:** _{int(float(sum))}_ aUEC.😢'
            else:
                return f'🏆 **Total profit:** _{int(float(sum))}_ aUEC.\n{percentageStr}\n(With an equal distribution of the ' \
                       f'profit, each person receives _{int(float(portion))}_ aUEC.💰)'
        except:
            return '❗Percentage breakdown could not be calculated. Please add expenses and incomes.'

    if message == '!help':
        return '**ℹ️ These are all available commands:** \n ```🔥Start or restart and clear user data: \n !start or !restart \n👤Add ' \
               'new user: \n !adduser <name> <amount of aUEC invested> \n🟥Add expense: \n !minus <amount of aUEC> ' \
               '<expense description> \n🟩Add revenue: \n !plus <amount of aUEC> <revenue description> \n🏆Get ' \
               'summary: \n !sum```'

    else:
        return '⚠️This is not a valid command.\nℹ️Try typing _"!help"_.'
