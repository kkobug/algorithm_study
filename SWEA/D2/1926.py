def clap():
    number = int(input())
    result = []
    for n in range(1, number+1):
        clap_time = ''

        for i in range(len(str(n))):
            if str(n)[i] in '369':
                clap_time += '-'

        if clap_time == '':
            clap_time = str(n)
            
        result.append(clap_time)
    return ' '.join(result)

print(clap())