import sublime, sublime_plugin

compJS = [
    ("req.params\treq", "req.params"),
    ("req.query\treq", "req.query"),
    ("req.body\treq", "req.body"),
    ("req.route\treq", "req.route"),
    ("req.cookies\treq", "req.cookies"),
    ("req.singnedCookies\treq", "req.singnedCookies"),
    ("req.accepts\treq", "req.accepts($1)"),
    ("req.ip\treq", "req.ip"),
    ("req.path\treq", "req.path"),
    ("req.host\treq", "req.host"),
    ("req.xhr\treq", "req.xhr"),
    ("req.protocol\treq", "req.protocol"),
    ("req.secure\treq", "req.secure"),
    ("req.url\treq", "req.url"),
    ("req.originalUrl\treq", "req.originalUrl"),
    ("req.acceptedLanguages\treq", "req.acceptedLanguages"),
    ("formdata\tContent-Type", "application/x-www-form-urlendcoded"),
    ("json\tContent-Type", "application/json"),
    ("res.status\tres", "res.status(${1:code})"),
    ("res.redirect\tres", "res.redirect(${1:url})"),
    ("res.send\tres", "res.send(${1:body})"),
    ("res.jsonp\tres", "res.jsonp(${1:json})"),
    ("res.json\tres", "res.json(${1:json})"),
    ("res.type\tres", "res.type(${1:type})"),
    ("res.sendFile\tres", "res.sendFile(${1:path,[option],[callback]})"),
    ("res.format\tres", "res.format(${1:object})"),
    ("res.render\tres", "res.render(${1:view,callback})"),
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