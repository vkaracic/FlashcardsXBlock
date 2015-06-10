"""
    Flashcards XBlock allowes the editor to add a list of quesitions and 
    answers (separated by a comma) which are then displayed as flashcards.
"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Dict, String
from xblock.fragment import Fragment

# Using the utils script from AnimationXBlock:
# https://github.com/pmitros/AnimationXBlock
# TO-DO: Create own

from .utils import render_template

class FlashcardsXBlock(XBlock):
    """
    The content (the values between the <flashcards> tags) is saved as a 
    dictionary and passed as a dictionary to the HTML template
    """
    title = String(
            default=u"Flashcards title",
            scope=Scope.settings,
            help=u"Title of the flashcards block"
        )

    content = Dict(
            default={},
            scope=Scope.settings,
            help=u"List of items"
        )


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    
    def student_view(self, context=None):
        """Create fragment and send the appropriate context."""
        context = {
            'flashcards': self.content,
            'title': self.title,
        }

        frag = Fragment()
        frag.add_content(render_template('static/html/flashcards.html', context))
        frag.add_css(self.resource_string("static/css/flashcards.css"))
        frag.add_javascript(self.resource_string("static/js/src/flashcards.js"))
        frag.initialize_js('FlashcardsXBlock')        
        return frag

    @classmethod
    def parse_xml(cls, node, runtime, keys, id_generator):
        """
        Parse the XML for an HTML block.

        The entire subtree under `node` is re-serialized, and set as the
        content of the XBlock.

        The content between the <flashcards> blocks is being transformed 
        into a dictionary, and as such saved into the content class variable
        (which is accessable with self.content)
        """
        block = runtime.construct_xblock_from_class(cls, keys)
        flashcards = {}
        
        for line in node.text.split('\n'):
            line = line.strip()
            line = line.split(',')
            if len(line) > 1:
                flashcards[line[0]] = line[1]

        block.content = flashcards
        block.title = node.attrib['title']
        return block


    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("FlashcardsXBlock",
             """<vertical_demo>
                <flashcards title="Capital cities">
Croatia,Zagreb
France,Paris
Lorem ipsum dolor sit amet vim ex simul soluta ponderum duo enim ornatus reprehendunt in ut nam dignissim theophrastus. Tacimates explicari ne sit dicit pertinax in est vel eu posse epicuri. Regione signiferumque mei in at sea rebum decore placerat. Eruditi voluptua in eum mei ex eleifend tractatos. Sed id summo consetetur reprehendunt ut nemore expetendis quo. Ex qui iisque nonumes fuisset., Lorem ipsum dolor sit amet vim ex simul soluta ponderum duo enim ornatus reprehendunt in ut nam dignissim theophrastus. Tacimates explicari ne sit dicit pertinax in est vel eu posse epicuri. Regione signiferumque mei in at sea rebum decore placerat. Eruditi voluptua in eum mei ex eleifend tractatos. Sed id summo consetetur reprehendunt ut nemore expetendis quo. Ex qui iisque nonumes fuisset.
                </flashcards>
                </vertical_demo>
             """),
        ]
