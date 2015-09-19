import sublime, sublime_plugin

compJS = [
    ("Events\tBackbone", "Backbone.Events"),
    ("Model\tBackbone", "Backbone.Model.extend({\n  $1\n})"),
    ("Collection\tBackbone", "Backbone.Collection.extend({model:$1})"),
    ("View\tBackbone", "Backbone.View.extend({\n  el:$1 ,\n  initialize: function() {\n  \n  },\n  events:{\n  \n  }\n})"),
    ("initialize\tBackbone", "initialize: function() {\n  $1\n}"),
    ("defaults\tBackbone", "defaults:{\n  $1\n}"),
    ("fetch\tBackbone", "fetch({\n   success: function(collection, response, options) {\n        $1\n    },\n    error: function(collection, response, options) {\n      \n  }\n});"),
    ("Router\tBackbone", "Backbone.Router.extend({\n  $1\n})"),
    ("routes\tBackbone", "routes:{\n  $1\n}"),
    ("start\tBackbone.history","start()"),
    ("JSON.stringify()","JSON.stringify()"),
    ("render\tBackbone","render:{\n  $1\n}"),
    ("listenTo\tbackbone","listenTo(${1:app.Todos, 'add', this.addOne});"),
    ("fetch","fetch();"),
    ("findWhere","findWhere($1)")
]

compAll = list(compJS)      # could use different lists

class AndyJSCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        global compAll
        if not (view.match_selector(locations[0],
                                    'source.js -string -comment -constant') or
                view.match_selector(locations[0],
                                    'source.ts -string -comment -constant')):
            return []
        completions = []
        pt = locations[0] - len(prefix) - 1
        # get the character before the trigger
        ch = view.substr(sublime.Region(pt, pt + 1)) if pt >= 0 else None
        if ch == '.': pass
        else: pass
        word = view.word(pt - 1) if pt >= 0 else None
        word = view.substr(word) if word is not None else None
        if word is not None and len(word) > 1:
            pass # could check for window or document
        completions = compAll
        compDefault = [view.extract_completions(prefix)]
        compDefault = [(item + "\tDefault", item) for sublist in compDefault 
            for item in sublist if len(item) > 3]       # flatten
        compDefault = list(set(compDefault))        # make unique
        compFull = list(completions)
        compFull.extend(compDefault)
        compFull.sort()
        return (compFull, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)