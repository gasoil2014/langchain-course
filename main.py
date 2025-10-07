from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
    Elon Reeve Musk (Pretoria, 28 de junio de 1971) es un empresario, inversor y magnate. Es el fundador, consejero delegado e «ingeniero» en jefe de la empresa SpaceX; inversor ángel, director general y arquitecto de productos de Tesla, Inc.; fundador de The Boring Company; y cofundador de Neuralink y OpenAI. Además, es el director de tecnología de X Corp. Entre enero y mayo de 2025, ejerció como administrador de facto del Departamento de Eficiencia Gubernamental de la Casa Blanca bajo la segunda presidencia de Donald Trump.

    Con un patrimonio neto estimado en unos cuatrocientos mil millones de dólares en diciembre de 2024,​ es la persona más rica del mundo según el índice de multimillonarios en tiempo real de Forbes.
    Musk nació y se crio en una rica familia de Pretoria (Sudáfrica). Su madre es canadiense y su padre un sudafricano blanco. Estudió brevemente en la Universidad de Pretoria antes de trasladarse a Canadá a los 17 años. Se matriculó en la Universidad de Queen y se trasladó a la Universidad de Pensilvania dos años después, donde se graduó en Economía y Física. En 1995 se trasladó a California para asistir a la Universidad Stanford, pero en su lugar decidió seguir una carrera empresarial, cofundando la empresa de software web Zip2 con su hermano Kimbal. Zip2 fue adquirida por Compaq por 307 millones de dólares en 1999. Ese mismo año, Musk cofundó el banco en línea X.com, que se fusionó con Confinity en 2000 para formar PayPal. La empresa fue comprada por eBay en 2002 por mil quinientos millones de dólares.

    En 2002, Musk fundó SpaceX, fabricante aeroespacial y empresa de servicios de transporte espacial, de la que es director general e ingeniero jefe. En 2003, se unió al fabricante de vehículos eléctricos Tesla Motors, Inc. (ahora Tesla, Inc.) como presidente y arquitecto de productos, convirtiéndose en su consejero delegado en 2008. En 2006, ayudó a crear SolarCity, una empresa de servicios de energía solar que posteriormente fue adquirida por Tesla y se convirtió en Tesla Energy. En 2015, cofundó OpenAI, una empresa de investigación sin ánimo de lucro que promueve la inteligencia artificial amigable. En 2016, cofundó Neuralink, una empresa de neuro tecnología centrada en el desarrollo de interfaces cerebro-ordenador, y fundó The Boring Company, una empresa de construcción de túneles. También acordó la compra de la importante red social estadounidense Twitter en 2022 por 44 000 millones de dólares. Musk también ha propuesto el hyperloop. En noviembre de 2021, el director general de Tesla fue la primera persona de la historia en acumular una fortuna de trescientos mil millones de dólares.

    Ha sido criticado por hacer declaraciones poco científicas y controvertidas. En 2018, fue demandado por la Comisión de Bolsa y Valores de Estados Unidos (SEC) por tuitear falsamente que había conseguido financiación para una adquisición privada de Tesla. Llegó a un acuerdo con la SEC, pero no admitió su culpabilidad, renunciando temporalmente a su presidencia y aceptando limitaciones en el uso de su Twitter personal. En 2019, ganó un juicio por difamación presentado contra él por un espeleólogo británico que asesoró en el rescate de la cueva Tham Luang. Musk también ha sido criticado por difundir información errónea sobre la pandemia de COVID-19 y teorías de conspiración; y por sus controvertidas opiniones sobre asuntos como la inteligencia artificial, las criptomonedas y el transporte público.
    """
    summary_template = """
    Given the information {information} about a person I want you to create:
    1) A short summary
    2) Three facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template 
    )

    llm = ChatOpenAI(model="gpt-5", temperature=0)
    #llm = ChatOllama(model="gpt-oss:20b", temperature=0)
    

    chain = summary_prompt_template | llm

    summary = chain.invoke({"information": information})
    
    print(summary.content)

if __name__ == "__main__":
    main()
