import sys
import syntax

if __name__ == "__main__":
    fi = syntax.nikiborg_lang(sys.argv[1])
    fi.run()
