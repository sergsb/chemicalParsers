from os.path import abspath, join, dirname

from pkg_resources import resource_stream, resource_filename
from py4j.java_gateway import JavaGateway, GatewayParameters, java_import

opsin = JavaGateway.launch_gateway(
    java_path=join(resource_filename('chemicalParsers',"jserver"), 'jre-10.0.1', 'bin', 'java'),
    classpath=join(resource_filename('chemicalParsers',"jserver"), 'opsin-2.3.1-jar-with-dependencies.jar'),
    die_on_exit=True)

chemTagger = JavaGateway.launch_gateway(
    java_path=abspath(join(dirname(__file__), 'jserver', 'jre-10.0.1', 'bin', 'java')),
    classpath=abspath(join(dirname(__file__), 'jserver', 'chemicalTagger-1.4.0-jar-with-dependencies.jar')),
    die_on_exit=True)

java_import(opsin.jvm, "uk.ac.cam.ch.wwmm.opsin.*")
java_import(chemTagger.jvm, 'uk.ac.cam.ch.wwmm.chemicaltagger.*')

nts = opsin.jvm.NameToStructure.getInstance()
tagger = chemTagger.jvm.ChemistryPOSTagger.getDefaultInstance()


def parseIUPACName(name):
    return nts.parseToSmiles(name)

def parseProtocol(text):
    chemistrySentenceParser = chemTagger.jvm.ChemistrySentenceParser(tagger.runTaggers(text))
    chemistrySentenceParser.parseTags()
    return str(chemistrySentenceParser.makeXMLDocument())

