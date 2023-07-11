import ast
import sys
import types

class _AstManager(types.ModuleType):
    # We overwrite the sys.modules entry for this function later, which will
    # cause all the values in globals() to be changed to None to allow garbage
    # collection. That forces us to do all of our imports into locals().
    class Lisp(ast.NodeTransformer):
        """Surround each statement with a try/except block to silence errors."""

        def generic_visit(self, node):
            import ast
            import sys
            ast.NodeTransformer.generic_visit(self, node)

            if isinstance(node, ast.stmt) and not isinstance(node, ast.FunctionDef):
                if sys.version_info[0] == 3:
                    new_node = ast.Try(
                        body=[node],
                        handlers=[ast.ExceptHandler(type=None,
                                                    name=None,
                                                    body=[ast.Pass()])],
                        orelse=[],
                        finalbody=[ast.Pass()])
                else:
                    new_node = ast.TryExcept(
                        body=[node],
                        handlers=[ast.ExceptHandler(type=None,
                                                    name=None,
                                                    body=[ast.Pass()])],
                        orelse=[])
                return ast.copy_location(new_node, node)
            return node