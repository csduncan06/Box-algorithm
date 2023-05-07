def Boxify(text):
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    box_top = '┌' + '─' * width + '┐'
    box_bottom = '└' + '─' * width + '┘'
    box_lines = ['│' + line.ljust(width) + '│' for line in lines]
    return '\n'.join([box_top] + box_lines + [box_bottom])


print(Boxify("This is Boxify\nA Python algorithm to generate a ASCII box around the given text!"))
