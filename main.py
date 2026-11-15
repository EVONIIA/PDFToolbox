"""Point d'entrée de PDF Toolbox by EVONIIA."""

from __future__ import annotations

import sys
from multiprocessing import freeze_support

from pdf_toolbox import ensure_python_version


if __name__ == "__main__":
    freeze_support()
    ensure_python_version()
    if "--verify-package" in sys.argv:
        from pdf_toolbox.package_check import verify_package

        index = sys.argv.index("--verify-package")
        report = sys.argv[index + 1] if index + 1 < len(sys.argv) else ""
        raise SystemExit(verify_package(report))
    from pdf_toolbox.app import main

    main()
