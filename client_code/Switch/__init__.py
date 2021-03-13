# MIT License
#
# Copyright (c) 2021 The Anvil Extras project team members listed at
# https://github.com/anvilistas/anvil-extras/graphs/contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# This software is published at https://github.com/anvilistas/anvil-extras
from .. import session
from ._anvil_designer import SwitchTemplate

__version__ = "1.0.0"

css = """
.anvil-role-switch {
   position: relative;
   width: 1.8em;
}

.anvil-role-switch input { 
  opacity: 0;
  height: 0;
}

.anvil-role-switch span {
   position: relative;
   display: block !important;
   font-size: ineherit;
}

.anvil-role-switch span::before {
   content: "";
   position: absolute;
   cursor: pointer;
   top: 0.1em;
   bottom: 0;
   left: -1em;
   width: 1.8em;
   height: 1em;
   background-color: #ccc;
   -webkit-transition: .4s;
   transition: .4s;
}

.anvil-role-switch span::after {
   position: absolute;
   cursor: pointer;
   content: "";
   height: .8em;
   width: .8em;
   left: -.88em;
   top: .2em;
   bottom: 0;
   background-color: white;
   -webkit-transition: .4s;
   transition: .4s;
}

.anvil-role-switch input:checked + span::after {
 -webkit-transform: translateX(.8em);
 -ms-transform: translateX(.8em);
 transform: translateX(.8em);
}

.anvil-role-switch span::after {
 border-radius: 50%;
}
.anvil-role-switch span::before {
 border-radius: .5em;
}
"""
session.style_injector.inject(css)
from anvil import CheckBox

class Switch(SwitchTemplate):
    def __init__(self, checked_color, **properties):
        print(properties)
        self.uid = session.get_uid()
        css = '\n'.join(self._get_css_rules(checked_color))
        self._sheet = session.style_injector.inject(css).sheet
        self.role = ["switch", f"switch-{self.uid}"]
        self.init_components(**properties)
        print(properties)
        print(checked_color)
        CheckBox.__init__(self, **properties)
    
    @property
    def checked_color(self):
        return self._checked_color

    @checked_color.setter
    def checked_color(self, value):
        for i in range(len(self._sheet.cssRules)):
          self._sheet.deleteRule(0)
        for rule in self._get_css_rules(value):
          self._sheet.insertRule(rule, 0)
        self._checked_color = value
      
    def _get_css_rules(self, checked_color):
      return (f".anvil-role-switch-{self.uid} input:checked + span::before {{background-color: {checked_color};}}",
              f".anvil-role-switch-{self.uid} input:focus + span::before {{box-shadow: 0 0 1px {checked_color};}}")


  

