Letter.destroy_all
# User.destroy_all
# Word.destroy_all
# Defination.destroy_all

# admin_user = User.create(first_name: 'Abu', last_name: 'Alghali', role: 2)
# ord_user = User.create(first_name: 'Joe', last_name: 'Alie', role: 0)

# glady = Word.create(title: 'Glady', user: ord_user, letter: letter_g)
# usai = Word.create(title: 'Usai', user: ord_user, letter: letter_u)
# kushe = Word.create(title: 'Kushɛh', user: ord_user, letter: letter_k)
# orihgt = Word.create(title: 'Ɔrayt', user: admin_user, letter: letter_or)
# kompin = Word.create(title: 'Kɔmpin', user: admin_user, letter: letter_k)

# Defination.create(define: 'Used to describe joy or excitement', example_statement: 'Ar gladi fɔ mit yu',
#                   approval_status: 1, user: admin_user, word: glady)
# Defination.create(define: 'Used to ask about a location or place', example_statement: 'Usai yu kɔmɔt?',
#                   approval_status: 1, user: admin_user, word: usai)
# Defination.create(define: 'A common way of saying hi or hello', example_statement: 'Kushɛh or Kushɛh-o',
#                   approval_status: 1, user: admin_user, word: kushe)
# Defination.create(define: 'Translates to yes or okay', example_statement: 'Yu ɔrayt?',
#                   approval_status: 1, user: admin_user, word: orihgt)
# Defination.create(define: 'Age mate or peers', example_statement: 'Na yu kɔmpin?',
#                   approval_status: 0, user: admin_user, word: kompin)

Letter.create(character: 'G')
Letter.create(character: 'U')
Letter.create(character: 'Ɔ')
Letter.create(character: 'K')
Letter.create(character: 'A')
Letter.create(character: 'Aw')
Letter.create(character: 'Ay')
Letter.create(character: 'B')
Letter.create(character: 'Ch')
Letter.create(character: 'D')
Letter.create(character: 'E')
Letter.create(character: 'Ɛ')
Letter.create(character: 'F')
Letter.create(character: 'Gb')
Letter.create(character: 'I')
Letter.create(character: 'J')
Letter.create(character: 'L')
Letter.create(character: 'M')
Letter.create(character: 'N')
Letter.create(character: 'Ny')
Letter.create(character: 'Ŋ')
Letter.create(character: 'O')
Letter.create(character: 'Ɔy')
Letter.create(character: 'P')
Letter.create(character: 'R')
Letter.create(character: 'S')
Letter.create(character: 'Sh')
Letter.create(character: 'T')
Letter.create(character: 'V')
Letter.create(character: 'W')
Letter.create(character: 'Y')
Letter.create(character: 'Z')
Letter.create(character: 'Zh')
