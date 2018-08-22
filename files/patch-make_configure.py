--- make/configure.py.orig	2018-08-22 10:41:00 UTC
+++ make/configure.py
@@ -1512,7 +1512,7 @@ try:
     class Tools:
         ar    = ToolProbe( 'AR.exe',    'ar', abort=True )
         cp    = ToolProbe( 'CP.exe',    'cp', abort=True )
-        gcc   = ToolProbe( 'GCC.gcc',   'gcc', IfHost( 'clang', '*-*-freebsd*' ), IfHost( 'gcc-4', '*-*-cygwin*' ))
+        gcc   = ToolProbe( 'GCC.gcc',   'gcc', IfHost( os.environ['CC'], '*-*-freebsd*' ), IfHost( 'clang', '*-*-freebsd*' ), IfHost( 'gcc-4', '*-*-cygwin*' ))
 
         if host.match( '*-*-darwin*' ):
             gmake = ToolProbe( 'GMAKE.exe', 'make', 'gmake', abort=True )
