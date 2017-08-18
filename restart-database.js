db.professores.remove({})
db.professores.insert({
	nome:'Marcia',
	sobrenome: 'Kazlenvsky',
	instituto: 'Instituto de Ciências Farmacêuticas',
	universidade: 'USP',
	area: 'Inibidores seletivos da recaptação de serotonina',
	pesquisas: [
		{_id: ObjectId(),
		titulo: 'Improvement of efficiency of sertraline production with calcium-hipercloryde as catalyst',
		inicio: 2002,
		fim: 2005,
		tags: ['sertraline', 'producion-efficiency', 'catalyst']}
	]})
db.professores.insert({
	nome:'Henrique',
	sobrenome: 'Custódio',
	instituto: 'Faculdade de Filosofia, Letras e Ciências Humanas',
	universidade: 'UFRB',
	area: 'Análise histórica do surgimento da semiótica pos-modernista',
	pesquisas: [
		{_id: ObjectId(),
		titulo: 'Criação das ',
		inicio: 2002,
		fim: 2005,
		tags: ['sertraline', 'producion-efficiency', 'catalyst']}
	]})
