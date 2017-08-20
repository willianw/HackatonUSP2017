db.pesquisadores.remove({})
db.pesquisadores.insert({
	_id: ObjectId("100000000000000000000000"),
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
db.pesquisadores.insert({
	_id: ObjectId("100000000000000000000001"),
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

db.instituicoes.insert({
	_id: ObjectId("200000000000000000000000"),
	nome: 'IME'
	localizacao: 'Sao Paulo'
})
