--- make/configure.py.orig	2018-06-17 04:23:34 UTC
+++ make/configure.py
@@ -1508,7 +1508,7 @@ try:
     class Tools:
         ar    = ToolProbe( 'AR.exe',    'ar', abort=True )
         cp    = ToolProbe( 'CP.exe',    'cp', abort=True )
-        gcc   = ToolProbe( 'GCC.gcc',   'gcc', IfHost( 'gcc-4', '*-*-cygwin*' ))
+        gcc   = ToolProbe( 'GCC.gcc',   'gcc', IfHost( os.environ['CC'], '*-*-freebsd*' ), IfHost( 'gcc-4', '*-*-cygwin*' ))
 
         if host.match( '*-*-darwin*' ):
             gmake = ToolProbe( 'GMAKE.exe', 'make', 'gmake', abort=True )
