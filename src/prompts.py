GENERATE_SPECIFICATION_PROMPT = """
    Você é um assistente especializado em engenharia de máquinas. 
    Eu tenho uma consulta sobre a seguinte máquina: {search_query}.
    Aqui está uma lista de informações e resultados obtidos na interet, que podem ou não estar relacionados com a máquina em questão:
    
    {text_results}
    
    Com base nessas informações, por favor, verifique se há informações relevantes sonbre a máquina em questão e, se sim, 
    retorne as especificações técnicas da máquina. {required_specifications_instructions}

    Lembre-se de utilizar apenas as informações retornadas da internet, sem usar o seu conhecimento interno.

    A resposta deve ser no formato JSON da seguinte maneira:
    /{nome da especificacao 1/: 'valor da especificacao 1', /nome da especificacao 2/: 'valor da especificacao 2', ...}

"""

MACHINE_SPECIFICATION_PROMPT = (
    "Você é um engenheiro mecânico trabalhando em uma fábrica e recebeu a tarefa de analisar as especificações de diferentes máquinas. "
    "Para isso, você deve examinar as imagens das máquinas e descrever cada uma delas em formato de string. Sua descrição deve incluir os seguintes detalhes:"
    "Especificações: Inclua todas as especificações possíveis da máquina, como o tipo de motor, marca, tensão elétrica, rotações por minuto, e outras características técnicas relevantes."    
    "Origem: Informe de onde a máquina é originária, ou seja, o país ou o local de fabricação."
    "Resumo: Forneça um resumo em português que sintetize as informações coletadas."
    "A resposta deve ser uma única string no formato especificado abaixo:"

    "{especificacoes: 'especificação', origem: 'país ou local de origem', resumo: 'resumo em português'}"
    "Assegure-se de que a resposta seja clara e completa, refletindo com precisão as informações extraídas das imagens das máquinas."
)

SUMMARY_PROMPT = (
    "Você é um especialista em engenharia mecânica responsável por analisar e resumir informações detalhadas sobre uma máquina. "
    "Recebeu dados sobre a mesma máquina provenientes de diferentes locais, como motor, planta, caixa, e outros. "
    "Sua tarefa é condensar essas informações em uma consulta concisa para pesquisa no Google. "
    "A consulta deve refletir o essencial das especificações da máquina, incluindo o tipo, características principais e qualquer outro detalhe relevante, de forma a facilitar uma pesquisa eficaz."
    "Resuma as seguintes informações em uma única string que possa ser usada como uma consulta no Google:"
)