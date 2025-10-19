list = [x for x in range(1,11) if not x % 2 == 0] 
print(list)


Recording = '''
Topic: සරල රේඛාව  
1. සරල රේඛාව විභාග ගැටලු  
2. සරල රේඛාව note එකට අදාළ ගැටලු  
3. සරල රේඛාව Day 01  
4. සරල රේඛාව 01  
5. සරල රේඛාව Day 02  
6. සරල රේඛාව 02  
7. සරල රේඛාව Day 03  
8. සරල රේඛාව 03  
9. සරල රේඛාව 04  
10. සරල රේඛාව 05 (video 1)  
11. සරල රේඛාව 05 (video 2)  

Topic: බලය  
1. බලය විභාග ගැටලු  
2. බලය home work ගැටලුව  
3. බලය VT home work ගැටලුව  
4. බලය 1992 ගණන  
5. බලය විභාග ගැටලු 2003  
6. බලය ll දෘඩ වස්තු Day 05(video 1)  
7. බලය ll දෘඩ වස්තු Day 05(video 2)  
8. බලය ll දෘඩ වස්තු Day 06 (video 1)  
9. බලය ll දෘඩ වස්තු Day 06 (video 2)  
10. බලය ll දෘඩ වස්තු Day 07 (vide01)  
11. බලය ll දෘඩ වස්තු Day 07 (vide02)  

Topic: අවකලනය  
1. අවකලන ප්‍රස්තාර විභාග ගැටලු  
2. අවකලනය යෙදීම විභාග ගැටලු  
3. අවකලනය යෙදීම් විභාග ගැටලු  

Topic: ප්‍රක්ශිප්ත  
1. ප්‍රක්ශිප්ත අමතර  
2. ප්‍රක්ශිප්ත Day 01  

Topic: ප්‍රවේගකාල ප්‍රස්තාර  
1. ප්‍රවේගකාල ප්‍රස්තාර විභාග ගැටලු  

Topic: Miscellaneous  
1. home work ගැටලු 2 හා cot ප්‍රමේය සම්බන්ධ ගැටලු  
2. Payement only

'''

for lesson in [text for text in Recording.splitlines() if not text.startswith('Topic') and not text == '']: print(lesson)
