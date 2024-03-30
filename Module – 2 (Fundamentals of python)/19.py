def test(s):
    try:
        not_poor = s.index('not')
        string_poor = s.index('poor')
        return s.replace(s[not_poor:(string_poor+4)], 'good')
    except ValueError:
        return s

print(test('The lyrics is not hap apa that poor!'))
print(test('The lyrics poor!'))
