import sublime, sublime_plugin

compNodejs = [
("require\tNodejs global", "require($0)"),
("ArrayBuffer()\tNodejs","ArrayBuffer()"),
("Int8Array()\tNodejs","Int8Array()"),
("Uint8Array()\tNodejs","Uint8Array()"),
("Int16Array()\tNodejs","Int16Array()"),
("Uint16Array()\tNodejs","Uint16Array()"),
("Int32Array()\tNodejs","Int32Array()"),
("Uint32Array()\tNodejs","Uint32Array()"),
("Float32Array()\tNodejs","Float32Array()"),
("Float64Array()\tNodejs","Float64Array()"),
("DataView()\tNodejs","DataView()"),
("Buffer(subject, encoding, offset)\tNodejs","Buffer(subject, encoding, offset)"),
("setTimeout(function, milliseconds)\tNodejs","setTimeout(${1:function}, ${2:milliseconds})"),
("setInterval()\tNodejs","setInterval(${1})"),
("clearTimeout()\tNodejs","clearTimeout()"),
("clearInterval()\tNodejs","clearInterval()"),
("process.EventEmitter()\tprocess","process.EventEmitter(${1})"),
("process.assert()\tprocess","process.assert(${1})"),
("process._tickCallback()\tprocess","process._tickCallback()"),
("process.nextTick(callback)\tprocess","process.nextTick(${1:callback})"),
("process.openStdin()\tprocess","process.openStdin()"),
("process.exit(code)\tprocess","process.exit(${1:code})"),
("process.kill(pid, sig)\tprocess","process.kill(pid, sig)"),
("process.addListener(type, listener)\tprocess","process.addListener(type, listener)"),
("process._needTickCallback()\tprocess","process._needTickCallback()"),
("process.on(type, listener)\tprocess","process.on(type, listener)"),
("process.removeListener(type, listener)\tprocess","process.removeListener(type, listener)"),
("process.reallyExit()\tprocess","process.reallyExit()"),
("process.debug()\tprocess","process.debug()"),
("process.chdir()\tprocess","process.chdir()"),
("process.cwd()\tprocess","process.cwd()"),
("process.error()\tprocess","process.error()"),
("process.umask()\tprocess","process.umask()"),
("process.watchFile()\tprocess","process.watchFile()"),
("process.getuid()\tprocess","process.getuid()"),
("process.unwatchFile()\tprocess","process.unwatchFile()"),
("process.mixin()\tprocess","process.mixin()"),
("process.setuid()\tprocess","process.setuid()"),
("process.setgid()\tprocess","process.setgid()"),
("process.createChildProcess()\tprocess","process.createChildProcess()"),
("process.getgid()\tprocess","process.getgid()"),
("process.inherits()\tprocess","process.inherits()"),
("process._kill()\tprocess","process._kill()"),
("process._byteLength()\tprocess","process._byteLength()"),
("process._debugProcess()\tprocess","process._debugProcess()"),
("process.dlopen()\tprocess","process.dlopen()"),
("process.uptime()\tprocess","process.uptime()"),
("process.memoryUsage()\tprocess","process.memoryUsage()"),
("process.uvCounters()\tprocess","process.uvCounters()"),
("process.binding()\tprocess","process.binding()"),
("process.setMaxListeners(n)\tprocess","process.setMaxListeners(n)"),
("process.emit()\tprocess","process.emit()"),
("process.once(type, listener)\tprocess","process.once(type, listener)"),
("process.removeAllListeners(type)\tprocess","process.removeAllListeners(type)"),
("process.listeners(type)\tprocess","process.listeners(type)"),
("require.resolve(request)\trequire","require.resolve(request)"),
("require.registerExtension()\trequire","require.registerExtension()"),
("_debugger.start(argv, stdin, stdout)\t_debugger","_debugger.start(${1:argv}, ${2:stdin}, ${3:stdout})$0"),
("_debugger.Protocol()\t_debugger","_debugger.Protocol()$0"),
("_debugger.Client()\t_debugger","_debugger.Client()$0"),
("_linklist.init(list)\t_linklist","_linklist.init(${1:list})$0"),
("_linklist.peek(list)\t_linklist","_linklist.peek(${1:list})$0"),
("_linklist.shift(list)\t_linklist","_linklist.shift(${1:list})$0"),
("_linklist.remove(item)\t_linklist","_linklist.remove(${1:item})$0"),
("_linklist.append(list, item)\t_linklist","_linklist.append(${1:list}, ${2:item})$0"),
("_linklist.isEmpty(list)\t_linklist","_linklist.isEmpty(${1:list})$0"),
("assert.AssertionError\tassert","assert.AssertionError(${1:AssertionErro})$0"),
("assert.fail(actual, expected, message, operator, stackStartFunction)\tassert","assert.fail(${1:actual}, ${2:expected}, ${3:message}, ${4:operator}, ${5:stackStartFunction})$0"),
("assert.ok(value, message)\tassert","assert.ok(${1:value}, ${2:message})$0"),
("assert.equal(actual, expected, message)\tassert","assert.equal(${1:actual}, ${2:expected}, ${3:message})$0"),
("assert.notEqual(actual, expected, message)\tassert","assert.notEqual(${1:actual}, ${2:expected}, ${3:message})$0"),
("assert.deepEqual(actual, expected, message)\tassert","assert.deepEqual(${1:actual}, ${2:expected}, ${3:message})$0"),
("assert.notDeepEqual(actual, expected, message)\tassert","assert.notDeepEqual(${1:actual}, ${2:expected}, ${3:message})$0"),
("assert.strictEqual(actual, expected, message)\tassert","assert.strictEqual(${1:actual}, ${2:expected}, ${3:message})$0"),
("assert.notStrictEqual(actual, expected, message)\tassert","assert.notStrictEqual(${1:actual}, ${2:expected}, ${3:message})$0"),
("assert.throws(block, /*optional*/error, /*optional*/message)\tassert","assert.throws(${1:block}, ${2:/*optional*/error}, ${3:/*optional*/message})$0"),
("assert.doesNotThrow(block, /*optional*/error, /*optional*/message)\tassert","assert.doesNotThrow(${1:block}, ${2:/*optional*/error}, ${3:/*optional*/message})$0"),
("assert.ifError(err)\tassert","assert.ifError(${1:err})$0"),
("buffer.SlowBuffer()\tbuffer","buffer.SlowBuffer()$0"),
("buffer.Buffer(subject, encoding, offset)\tbuffer","buffer.Buffer(${1:subject}, ${2:encoding}, ${3:offset})$0"),
("buffer_ieee754.readIEEE754(buffer, offset, isBE, mLen, nBytes)\tbuffer_ieee754","buffer_ieee754.readIEEE754(${1:buffer}, ${2:offset}, ${3:isBE}, ${4:mLen}, ${5:nBytes})$0"),
("buffer_ieee754.writeIEEE754(buffer, value, offset, isBE, mLen, nBytes)\tbuffer_ieee754","buffer_ieee754.writeIEEE754(${1:buffer}, ${2:value}, ${3:offset}, ${4:isBE}, ${5:mLen}, ${6:nBytes})$0"),
("child_process.fork(modulePath, args, options)\tchild_process","child_process.fork(${1:modulePath}, ${2:args}, ${3:options})$0"),
("child_process._forkChild()\tchild_process","child_process._forkChild()$0"),
("child_process.exec(command /*, options, callback */)\tchild_process","child_process.exec(${1:command}, ${2:/*}, ${3:options}, ${4:callback}, ${5:*/})$0"),
("child_process.execFile(file /* args, options, callback */)\tchild_process","child_process.execFile(${1:file}, ${2:/*}, ${3:args}, ${4:options}, ${5:callback}, ${6:*/})$0"),
("child_process.spawn(file, args, options)\tchild_process","child_process.spawn(${1:file}, ${2:args}, ${3:options})$0"),
("cluster.fork()\tcluster","cluster.fork()$0"),
("cluster._startWorker()\tcluster","cluster._startWorker()$0"),
("cluster._getServer(address, port, addressType, cb)\tcluster","cluster._getServer(${1:address}, ${2:port}, ${3:addressType}, ${4:cb})$0"),
("cluster.setMaxListeners(n)\tcluster","cluster.setMaxListeners(${1:n})$0"),
("cluster.emit()\tcluster","cluster.emit()$0"),
("cluster.addListener(type, listener)\tcluster","cluster.addListener(${1:type}, ${2:listener})$0"),
("cluster.on(type, listener)\tcluster","cluster.on(${1:type}, ${2:listener})$0"),
("cluster.once(type, listener)\tcluster","cluster.once(${1:type}, ${2:listener})$0"),
("cluster.removeListener(type, listener)\tcluster","cluster.removeListener(${1:type}, ${2:listener})$0"),
("cluster.removeAllListeners(type)\tcluster","cluster.removeAllListeners(${1:type})$0"),
("cluster.listeners(type)\tcluster","cluster.listeners(${1:type})$0"),
("console.log(message)\tconsole","console.log(${1:message})$0"),
("console.info(message)\tconsole","console.info(${1:message})$0"),
("console.warn(message)\tconsole","console.warn(${1:message})$0"),
("console.error(message)\tconsole","console.error(${1:message})$0"),
("console.dir(object)\tconsole","console.dir(${1:object})$0"),
("console.time(label)\tconsole","console.time(${1:label})$0"),
("console.timeEnd(label)\tconsole","console.timeEnd(${1:label})$0"),
("console.trace(label)\tconsole","console.trace(${1:label})$0"),
("console.assert(expression)\tconsole","console.assert(${1:expression})$0"),
("crypto.Credentials(secureProtocol, flags, context)\tcrypto","crypto.Credentials(${1:secureProtocol}, ${2:flags}, ${3:context})$0"),
("crypto.createCredentials(options, context)\tcrypto","crypto.createCredentials(${1:options}, ${2:context})$0"),
("crypto.Hash()\tcrypto","crypto.Hash()$0"),
("crypto.createHash(hash)\tcrypto","crypto.createHash(${1:hash})$0"),
("crypto.Hmac()\tcrypto","crypto.Hmac()$0"),
("crypto.createHmac(hmac, key)\tcrypto","crypto.createHmac(${1:hmac}, ${2:key})$0"),
("crypto.Cipher()\tcrypto","crypto.Cipher()$0"),
("crypto.createCipher(cipher, password)\tcrypto","crypto.createCipher(${1:cipher}, ${2:password})$0"),
("crypto.createCipheriv(cipher, key, iv)\tcrypto","crypto.createCipheriv(${1:cipher}, ${2:key}, ${3:iv})$0"),
("crypto.Decipher()\tcrypto","crypto.Decipher()$0"),
("crypto.createDecipher(cipher, password)\tcrypto","crypto.createDecipher(${1:cipher}, ${2:password})$0"),
("crypto.createDecipheriv(cipher, key, iv)\tcrypto","crypto.createDecipheriv(${1:cipher}, ${2:key}, ${3:iv})$0"),
("crypto.Sign()\tcrypto","crypto.Sign()$0"),
("crypto.createSign(algorithm)\tcrypto","crypto.createSign(${1:algorithm})$0"),
("crypto.Verify()\tcrypto","crypto.Verify()$0"),
("crypto.createVerify(algorithm)\tcrypto","crypto.createVerify(${1:algorithm})$0"),
("crypto.DiffieHellman()\tcrypto","crypto.DiffieHellman()$0"),
("crypto.createDiffieHellman(size_or_key, enc)\tcrypto","crypto.createDiffieHellman(${1:size_or_key}, ${2:enc})$0"),
("crypto.pbkdf2()\tcrypto","crypto.pbkdf2()$0"),
("crypto.randomBytes()\tcrypto","crypto.randomBytes()$0"),
("crypto.pseudoRandomBytes()\tcrypto","crypto.pseudoRandomBytes()$0"),
("crypto.rng()\tcrypto","crypto.rng()$0"),
("crypto.prng()\tcrypto","crypto.prng()$0"),
("dgram.Socket(type, listener)\tdgram","dgram.Socket(${1:type}, ${2:listener})$0"),
("dgram.createSocket(type, listener)\tdgram","dgram.createSocket(${1:type}, ${2:listener})$0"),
("dns.lookup(domain, family, callback)\tdns","dns.lookup(${1:domain}, ${2:family}, ${3:callback})$0"),
("dns.resolve4(name, callback)\tdns","dns.resolve4(${1:name}, ${2:callback})$0"),
("dns.resolve6(name, callback)\tdns","dns.resolve6(${1:name}, ${2:callback})$0"),
("dns.resolveCname(name, callback)\tdns","dns.resolveCname(${1:name}, ${2:callback})$0"),
("dns.resolveMx(name, callback)\tdns","dns.resolveMx(${1:name}, ${2:callback})$0"),
("dns.resolveNs(name, callback)\tdns","dns.resolveNs(${1:name}, ${2:callback})$0"),
("dns.resolveTxt(name, callback)\tdns","dns.resolveTxt(${1:name}, ${2:callback})$0"),
("dns.resolveSrv(name, callback)\tdns","dns.resolveSrv(${1:name}, ${2:callback})$0"),
("dns.reverse(name, callback)\tdns","dns.reverse(${1:name}, ${2:callback})$0"),
("dns.resolve(domain, type_, callback_)\tdns","dns.resolve(${1:domain}, ${2:type_}, ${3:callback_})$0"),
("events.EventEmitter()\tevents","events.EventEmitter()$0"),
("freelist.FreeList(name, max, constructor)\tfreelist","freelist.FreeList(${1:name}, ${2:max}, ${3:constructor})$0"),
("fs.Stats()\tfs","fs.Stats()$0"),
("fs.readFile(path, encoding_)\tfs","fs.readFile(${1:path}, ${2:encoding_})$0"),
("fs.readFileSync(path, encoding)\tfs","fs.readFileSync(${1:path}, ${2:encoding})$0"),
("fs.close(fd, callback)\tfs","fs.close(${1:fd}, ${2:callback})$0"),
("fs.closeSync(fd)\tfs","fs.closeSync(${1:fd})$0"),
("fs.exists(path, callback)\tfs","fs.exists(${1:path}, ${2:callback})$0"),
("fs.existsSync(path)\tfs","fs.existsSync(${1:path})$0"),
("fs.open(path, flags, mode, callback)\tfs","fs.open(${1:path}, ${2:flags}, ${3:mode}, ${4:callback})$0"),
("fs.openSync(path, flags, mode)\tfs","fs.openSync(${1:path}, ${2:flags}, ${3:mode})$0"),
("fs.read(fd, buffer, offset, length, position, callback)\tfs","fs.read(${1:fd}, ${2:buffer}, ${3:offset}, ${4:length}, ${5:position}, ${6:callback})$0"),
("fs.readSync(fd, buffer, offset, length, position)\tfs","fs.readSync(${1:fd}, ${2:buffer}, ${3:offset}, ${4:length}, ${5:position})$0"),
("fs.write(fd, buffer, offset, length, position, callback)\tfs","fs.write(${1:fd}, ${2:buffer}, ${3:offset}, ${4:length}, ${5:position}, ${6:callback})$0"),
("fs.writeSync(fd, buffer, offset, length, position)\tfs","fs.writeSync(${1:fd}, ${2:buffer}, ${3:offset}, ${4:length}, ${5:position})$0"),
("fs.rename(oldPath, newPath, callback)\tfs","fs.rename(${1:oldPath}, ${2:newPath}, ${3:callback})$0"),
("fs.renameSync(oldPath, newPath)\tfs","fs.renameSync(${1:oldPath}, ${2:newPath})$0"),
("fs.truncate(fd, len, callback)\tfs","fs.truncate(${1:fd}, ${2:len}, ${3:callback})$0"),
("fs.truncateSync(fd, len)\tfs","fs.truncateSync(${1:fd}, ${2:len})$0"),
("fs.rmdir(path, callback)\tfs","fs.rmdir(${1:path}, ${2:callback})$0"),
("fs.rmdirSync(path)\tfs","fs.rmdirSync(${1:path})$0"),
("fs.fdatasync(fd, callback)\tfs","fs.fdatasync(${1:fd}, ${2:callback})$0"),
("fs.fdatasyncSync(fd)\tfs","fs.fdatasyncSync(${1:fd})$0"),
("fs.fsync(fd, callback)\tfs","fs.fsync(${1:fd}, ${2:callback})$0"),
("fs.fsyncSync(fd)\tfs","fs.fsyncSync(${1:fd})$0"),
("fs.mkdir(path, mode, callback)\tfs","fs.mkdir(${1:path}, ${2:mode}, ${3:callback})$0"),
("fs.mkdirSync(path, mode)\tfs","fs.mkdirSync(${1:path}, ${2:mode})$0"),
("fs.sendfile(outFd, inFd, inOffset, length, callback)\tfs","fs.sendfile(${1:outFd}, ${2:inFd}, ${3:inOffset}, ${4:length}, ${5:callback})$0"),
("fs.sendfileSync(outFd, inFd, inOffset, length)\tfs","fs.sendfileSync(${1:outFd}, ${2:inFd}, ${3:inOffset}, ${4:length})$0"),
("fs.readdir(path, callback)\tfs","fs.readdir(${1:path}, ${2:callback})$0"),
("fs.readdirSync(path)\tfs","fs.readdirSync(${1:path})$0"),
("fs.fstat(fd, callback)\tfs","fs.fstat(${1:fd}, ${2:callback})$0"),
("fs.lstat(path, callback)\tfs","fs.lstat(${1:path}, ${2:callback})$0"),
("fs.stat(path, callback)\tfs","fs.stat(${1:path}, ${2:callback})$0"),
("fs.fstatSync(fd)\tfs","fs.fstatSync(${1:fd})$0"),
("fs.lstatSync(path)\tfs","fs.lstatSync(${1:path})$0"),
("fs.statSync(path)\tfs","fs.statSync(${1:path})$0"),
("fs.readlink(path, callback)\tfs","fs.readlink(${1:path}, ${2:callback})$0"),
("fs.readlinkSync(path)\tfs","fs.readlinkSync(${1:path})$0"),
("fs.symlink(destination, path, type_, callback)\tfs","fs.symlink(${1:destination}, ${2:path}, ${3:type_}, ${4:callback})$0"),
("fs.symlinkSync(destination, path, type)\tfs","fs.symlinkSync(${1:destination}, ${2:path}, ${3:type})$0"),
("fs.link(srcpath, dstpath, callback)\tfs","fs.link(${1:srcpath}, ${2:dstpath}, ${3:callback})$0"),
("fs.linkSync(srcpath, dstpath)\tfs","fs.linkSync(${1:srcpath}, ${2:dstpath})$0"),
("fs.unlink(path, callback)\tfs","fs.unlink(${1:path}, ${2:callback})$0"),
("fs.unlinkSync(path)\tfs","fs.unlinkSync(${1:path})$0"),
("fs.fchmod(fd, mode, callback)\tfs","fs.fchmod(${1:fd}, ${2:mode}, ${3:callback})$0"),
("fs.fchmodSync(fd, mode)\tfs","fs.fchmodSync(${1:fd}, ${2:mode})$0"),
("fs.chmod(path, mode, callback)\tfs","fs.chmod(${1:path}, ${2:mode}, ${3:callback})$0"),
("fs.chmodSync(path, mode)\tfs","fs.chmodSync(${1:path}, ${2:mode})$0"),
("fs.fchown(fd, uid, gid, callback)\tfs","fs.fchown(${1:fd}, ${2:uid}, ${3:gid}, ${4:callback})$0"),
("fs.fchownSync(fd, uid, gid)\tfs","fs.fchownSync(${1:fd}, ${2:uid}, ${3:gid})$0"),
("fs.chown(path, uid, gid, callback)\tfs","fs.chown(${1:path}, ${2:uid}, ${3:gid}, ${4:callback})$0"),
("fs.chownSync(path, uid, gid)\tfs","fs.chownSync(${1:path}, ${2:uid}, ${3:gid})$0"),
("fs._toUnixTimestamp(time)\tfs","fs._toUnixTimestamp(${1:time})$0"),
("fs.utimes(path, atime, mtime, callback)\tfs","fs.utimes(${1:path}, ${2:atime}, ${3:mtime}, ${4:callback})$0"),
("fs.utimesSync(path, atime, mtime)\tfs","fs.utimesSync(${1:path}, ${2:atime}, ${3:mtime})$0"),
("fs.futimes(fd, atime, mtime, callback)\tfs","fs.futimes(${1:fd}, ${2:atime}, ${3:mtime}, ${4:callback})$0"),
("fs.futimesSync(fd, atime, mtime)\tfs","fs.futimesSync(${1:fd}, ${2:atime}, ${3:mtime})$0"),
("fs.writeFile(path, data, encoding_, callback)\tfs","fs.writeFile(${1:path}, ${2:data}, ${3:encoding_}, ${4:callback})$0"),
("fs.writeFileSync(path, data, encoding)\tfs","fs.writeFileSync(${1:path}, ${2:data}, ${3:encoding})$0"),
("fs.watch(filename)\tfs","fs.watch(${1:filename})$0"),
("fs.watchFile(filename)\tfs","fs.watchFile(${1:filename})$0"),
("fs.unwatchFile(filename)\tfs","fs.unwatchFile(${1:filename})$0"),
("fs.realpathSync(p, cache)\tfs","fs.realpathSync(${1:p}, ${2:cache})$0"),
("fs.realpath(p, cache, cb)\tfs","fs.realpath(${1:p}, ${2:cache}, ${3:cb})$0"),
("fs.createReadStream(path, options)\tfs","fs.createReadStream(${1:path}, ${2:options})$0"),
("fs.ReadStream(path, options)\tfs","fs.ReadStream(${1:path}, ${2:options})$0"),
("fs.FileReadStream(path, options)\tfs","fs.FileReadStream(${1:path}, ${2:options})$0"),
("fs.createWriteStream(path, options)\tfs","fs.createWriteStream(${1:path}, ${2:options})$0"),
("fs.WriteStream(path, options)\tfs","fs.WriteStream(${1:path}, ${2:options})$0"),
("fs.FileWriteStream(path, options)\tfs","fs.FileWriteStream(${1:path}, ${2:options})$0"),
("fs.SyncWriteStream(fd)\tfs","fs.SyncWriteStream(${1:fd})$0"),
("http.IncomingMessage(socket)\thttp","http.IncomingMessage(${1:socket})$0"),
("http.OutgoingMessage()\thttp","http.OutgoingMessage()$0"),
("http.ServerResponse(req)\thttp","http.ServerResponse(${1:req})$0"),
("http.Agent(options)\thttp","http.Agent(${1:options})$0"),
("http.ClientRequest(options, cb)\thttp","http.ClientRequest(${1:options}, ${2:cb})$0"),
("http.request(options, cb)\thttp","http.request(${1:options}, ${2:cb})$0"),
("http.get(options, cb)\thttp","http.get(${1:options}, ${2:cb})$0"),
("http.Server(requestListener)\thttp","http.Server(${1:requestListener})$0"),
("http.createServer(requestListener)\thttp","http.createServer(${1:requestListener})$0"),
("http._connectionListener(socket)\thttp","http._connectionListener(${1:socket})$0"),
("http.Client(port, host)\thttp","http.Client(${1:port}, ${2:host})$0"),
("http.createClient(port, host)\thttp","http.createClient(${1:port}, ${2:host})$0"),
("https.Server(opts, requestListener)\thttps","https.Server(${1:opts}, ${2:requestListener})$0"),
("https.createServer(opts, requestListener)\thttps","https.createServer(${1:opts}, ${2:requestListener})$0"),
("https.Agent(options)\thttps","https.Agent(${1:options})$0"),
("https.request(options, cb)\thttps","https.request(${1:options}, ${2:cb})$0"),
("https.get(options, cb)\thttps","https.get(${1:options}, ${2:cb})$0"),
("module.wrap(script)\tmodule","module.wrap(${1:script})$0"),
("module._debug()\tmodule","module._debug()$0"),
("module._findPath(request, paths)\tmodule","module._findPath(${1:request}, ${2:paths})$0"),
("module._nodeModulePaths(from)\tmodule","module._nodeModulePaths(${1:from})$0"),
("module._resolveLookupPaths(request, parent)\tmodule","module._resolveLookupPaths(${1:request}, ${2:parent})$0"),
("module._load(request, parent, isMain)\tmodule","module._load(${1:request}, ${2:parent}, ${3:isMain})$0"),
("module._resolveFilename(request, parent)\tmodule","module._resolveFilename(${1:request}, ${2:parent})$0"),
("module.runMain()\tmodule","module.runMain()$0"),
("module._initPaths()\tmodule","module._initPaths()$0"),
("module.requireRepl()\tmodule","module.requireRepl()$0"),
("module.Module(id, parent)\tmodule","module.Module(${1:id}, ${2:parent})$0"),
("net.createServer()\tnet","net.createServer()$0"),
("net.createConnection(port /* [host], [cb] */)\tnet","net.createConnection(${1:port}, ${2:/*}, ${3:[host]}, ${4:[cb]}, ${5:*/})$0"),
("net.connect(port /* [host], [cb] */)\tnet","net.connect(${1:port}, ${2:/*}, ${3:[host]}, ${4:[cb]}, ${5:*/})$0"),
("net.Socket(options)\tnet","net.Socket(${1:options})$0"),
("net.Stream(options)\tnet","net.Stream(${1:options})$0"),
("net.Server(/* [ options, ] listener */)\tnet","net.Server(${1:/*}, ${2:[}, ${3:options}, ${4:]}, ${5:listener}, ${6:*/})$0"),
("net._createServerHandle(address, port, addressType)\tnet","net._createServerHandle(${1:address}, ${2:port}, ${3:addressType})$0"),
("net.isIP(input)\tnet","net.isIP(${1:input})$0"),
("net.isIPv4(input)\tnet","net.isIPv4(${1:input})$0"),
("net.isIPv6(input)\tnet","net.isIPv6(${1:input})$0"),
("os.hostname()\tos","os.hostname()$0"),
("os.loadavg()\tos","os.loadavg()$0"),
("os.uptime()\tos","os.uptime()$0"),
("os.freemem()\tos","os.freemem()$0"),
("os.totalmem()\tos","os.totalmem()$0"),
("os.cpus()\tos","os.cpus()$0"),
("os.type()\tos","os.type()$0"),
("os.release()\tos","os.release()$0"),
("os.networkInterfaces()\tos","os.networkInterfaces()$0"),
("os.arch()\tos","os.arch()$0"),
("os.platform()\tos","os.platform()$0"),
("os.getNetworkInterfaces()\tos","os.getNetworkInterfaces()$0"),
("path.resolve()\tpath","path.resolve()$0"),
("path.normalize(path)\tpath","path.normalize(${1:path})$0"),
("path.join()\tpath","path.join()$0"),
("path.relative(from, to)\tpath","path.relative(${1:from}, ${2:to})$0"),
("path.dirname(path)\tpath","path.dirname(${1:path})$0"),
("path.basename(path, ext)\tpath","path.basename(${1:path}, ${2:ext})$0"),
("path.extname(path)\tpath","path.extname(${1:path})$0"),
("path._makeLong(path)\tpath","path._makeLong(${1:path})$0"),
("punycode.decode(input)\tpunycode","punycode.decode(${1:input})$0"),
("punycode.encode(input)\tpunycode","punycode.encode(${1:input})$0"),
("punycode.toASCII(domain)\tpunycode","punycode.toASCII(${1:domain})$0"),
("punycode.toUnicode(domain)\tpunycode","punycode.toUnicode(${1:domain})$0"),
("querystring.unescapeBuffer(s, decodeSpaces)\tquerystring","querystring.unescapeBuffer(${1:s}, ${2:decodeSpaces})$0"),
("querystring.unescape(s, decodeSpaces)\tquerystring","querystring.unescape(${1:s}, ${2:decodeSpaces})$0"),
("querystring.escape(str)\tquerystring","querystring.escape(${1:str})$0"),
("querystring.encode(obj, sep, eq, name)\tquerystring","querystring.encode(${1:obj}, ${2:sep}, ${3:eq}, ${4:name})$0"),
("querystring.stringify(obj, sep, eq, name)\tquerystring","querystring.stringify(${1:obj}, ${2:sep}, ${3:eq}, ${4:name})$0"),
("querystring.decode(qs, sep, eq)\tquerystring","querystring.decode(${1:qs}, ${2:sep}, ${3:eq})$0"),
("querystring.parse(qs, sep, eq)\tquerystring","querystring.parse(${1:qs}, ${2:sep}, ${3:eq})$0"),
("readline.createInterface(input, output, completer)\treadline","readline.createInterface(${1:input}, ${2:output}, ${3:completer})$0"),
("readline.Interface(input, output, completer)\treadline","readline.Interface(${1:input}, ${2:output}, ${3:completer})$0"),
("repl.writer(obj, showHidden, depth, colors)\trepl","repl.writer(${1:obj}, ${2:showHidden}, ${3:depth}, ${4:colors})$0"),
("repl.REPLServer(prompt, stream, eval, useGlobal, ignoreUndefined)\trepl","repl.REPLServer(${1:prompt}, ${2:stream}, ${3:eval}, ${4:useGlobal}, ${5:ignoreUndefined})$0"),
("repl.start(prompt, source, eval, useGlobal, ignoreUndefined)\trepl","repl.start(${1:prompt}, ${2:source}, ${3:eval}, ${4:useGlobal}, ${5:ignoreUndefined})$0"),
("stream.super_()\tstream","stream.super_()$0"),
("stream.Stream()\tstream","stream.Stream()$0"),
("string_decoder.StringDecoder(encoding)\tstring_decoder","string_decoder.StringDecoder(${1:encoding})$0"),
("sys.print()\tsys","sys.print()$0"),
("sys.puts()\tsys","sys.puts()$0"),
("sys.debug(x)\tsys","sys.debug(${1:x})$0"),
("sys.error(x)\tsys","sys.error(${1:x})$0"),
("sys.inspect(obj, showHidden, depth, colors)\tsys","sys.inspect(${1:obj}, ${2:showHidden}, ${3:depth}, ${4:colors})$0"),
("sys.p()\tsys","sys.p()$0"),
("sys.log(msg)\tsys","sys.log(${1:msg})$0"),
("sys.exec()\tsys","sys.exec()$0"),
("sys.pump(readStream, writeStream, callback)\tsys","sys.pump(${1:readStream}, ${2:writeStream}, ${3:callback})$0"),
("sys.inherits(ctor, superCtor)\tsys","sys.inherits(${1:ctor}, ${2:superCtor})$0"),
("timers.unenroll(item)\ttimers","timers.unenroll(${1:item})$0"),
("timers.enroll(item, msecs)\ttimers","timers.enroll(${1:item}, ${2:msecs})$0"),
("timers.active(item)\ttimers","timers.active(${1:item})$0"),
("timers.setTimeout(callback, after)\ttimers","timers.setTimeout(${1:callback}, ${2:after})$0"),
("timers.clearTimeout(timer)\ttimers","timers.clearTimeout(${1:timer})$0"),
("timers.setInterval(callback, repeat)\ttimers","timers.setInterval(${1:callback}, ${2:repeat})$0"),
("timers.clearInterval(timer)\ttimers","timers.clearInterval(${1:timer})$0"),
("tls.createSecurePair(credentials,isServer,requestCert,rejectUnauthorized)\ttls","tls.createSecurePair(${1:credentials}, ${2:}, ${3:isServer}, ${4:}, ${5:requestCert}, ${6:}, ${7:rejectUnauthorized})$0"),
("tls.Server(/* [options], listener */)\ttls","tls.Server(${1:/*}, ${2:[options]}, ${3:listener}, ${4:*/})$0"),
("tls.createServer(options, listener)\ttls","tls.createServer(${1:options}, ${2:listener})$0"),
("tls.connect(port /* host, options, cb */)\ttls","tls.connect(${1:port}, ${2:/*}, ${3:host}, ${4:options}, ${5:cb}, ${6:*/})$0"),
("tty.isatty(fd)\ttty","tty.isatty(${1:fd})$0"),
("tty.setRawMode(flag)\ttty","tty.setRawMode(${1:flag})$0"),
("tty.getWindowSize()\ttty","tty.getWindowSize()$0"),
("tty.setWindowSize()\ttty","tty.setWindowSize()$0"),
("tty.ReadStream(fd)\ttty","tty.ReadStream(${1:fd})$0"),
("tty.WriteStream(fd)\ttty","tty.WriteStream(${1:fd})$0"),
("url.parse(url, parseQueryString, slashesDenoteHost)\turl","url.parse(${1:url}, ${2:parseQueryString}, ${3:slashesDenoteHost})$0"),
("url.resolve(source, relative)\turl","url.resolve(${1:source}, ${2:relative})$0"),
("url.resolveObject(source, relative)\turl","url.resolveObject(${1:source}, ${2:relative})$0"),
("url.format(obj)\turl","url.format(${1:obj})$0"),
("util.format(f)\tutil","util.format(${1:f})$0"),
("util.print()\tutil","util.print()$0"),
("util.puts()\tutil","util.puts()$0"),
("util.debug(x)\tutil","util.debug(${1:x})$0"),
("util.error(x)\tutil","util.error(${1:x})$0"),
("util.inspect(obj, showHidden, depth, colors)\tutil","util.inspect(${1:obj}, ${2:showHidden}, ${3:depth}, ${4:colors})$0"),
("util.isArray(ar)\tutil","util.isArray(${1:ar})$0"),
("util.isRegExp(re)\tutil","util.isRegExp(${1:re})$0"),
("util.isDate(d)\tutil","util.isDate(${1:d})$0"),
("util.isError(e)\tutil","util.isError(${1:e})$0"),
("util.p()\tutil","util.p()$0"),
("util.log(msg)\tutil","util.log(${1:msg})$0"),
("util.exec()\tutil","util.exec()$0"),
("util.pump(readStream, writeStream, callback)\tutil","util.pump(${1:readStream}, ${2:writeStream}, ${3:callback})$0"),
("util.inherits(ctor, superCtor)\tutil","util.inherits(${1:ctor}, ${2:superCtor})$0"),
("util._deprecationWarning(moduleId, message)\tutil","util._deprecationWarning(${1:moduleId}, ${2:message})$0"),
("vm.Script()\tvm","vm.Script()$0"),
("vm.createScript(code, ctx, name)\tvm","vm.createScript(${1:code}, ${2:ctx}, ${3:name})$0"),
("vm.createContext()\tvm","vm.createContext()$0"),
("vm.runInContext()\tvm","vm.runInContext()$0"),
("vm.runInThisContext()\tvm","vm.runInThisContext()$0"),
("vm.runInNewContext()\tvm","vm.runInNewContext()$0"),
("zlib.Zlib()\tzlib","zlib.Zlib()$0"),
("zlib.Deflate(opts)\tzlib","zlib.Deflate(${1:opts})$0"),
("zlib.Inflate(opts)\tzlib","zlib.Inflate(${1:opts})$0"),
("zlib.Gzip(opts)\tzlib","zlib.Gzip(${1:opts})$0"),
("zlib.Gunzip(opts)\tzlib","zlib.Gunzip(${1:opts})$0"),
("zlib.DeflateRaw(opts)\tzlib","zlib.DeflateRaw(${1:opts})$0"),
("zlib.InflateRaw(opts)\tzlib","zlib.InflateRaw(${1:opts})$0"),
("zlib.Unzip(opts)\tzlib","zlib.Unzip(${1:opts})$0"),
("zlib.createDeflate(o)\tzlib","zlib.createDeflate(${1:o})$0"),
("zlib.createInflate(o)\tzlib","zlib.createInflate(${1:o})$0"),
("zlib.createDeflateRaw(o)\tzlib","zlib.createDeflateRaw(${1:o})$0"),
("zlib.createInflateRaw(o)\tzlib","zlib.createInflateRaw(${1:o})$0"),
("zlib.createGzip(o)\tzlib","zlib.createGzip(${1:o})$0"),
("zlib.createGunzip(o)\tzlib","zlib.createGunzip(${1:o})$0"),
("zlib.createUnzip(o)\tzlib","zlib.createUnzip(${1:o})$0"),
("zlib.deflate(buffer, callback)\tzlib","zlib.deflate(${1:buffer}, ${2:callback})$0"),
("zlib.gzip(buffer, callback)\tzlib","zlib.gzip(${1:buffer}, ${2:callback})$0"),
("zlib.deflateRaw(buffer, callback)\tzlib","zlib.deflateRaw(${1:buffer}, ${2:callback})$0"),
("zlib.unzip(buffer, callback)\tzlib","zlib.unzip(${1:buffer}, ${2:callback})$0"),
("zlib.inflate(buffer, callback)\tzlib","zlib.inflate(${1:buffer}, ${2:callback})$0"),
("zlib.gunzip(buffer, callback)\tzlib","zlib.gunzip(${1:buffer}, ${2:callback})$0"),
("zlib.inflateRaw(buffer, callback)\tzlib","zlib.inflateRaw(${1:buffer}, ${2:callback})$0")
]

compAll = list(compNodejs)      # could use different lists

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