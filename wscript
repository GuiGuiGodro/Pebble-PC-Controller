
<<<<<<< HEAD
#
=======
    #
>>>>>>> bcd2b063ddbd23b694f6f2dba8060f7238354dd2
# This file is the default set of rules to compile a Pebble project.
#
# Feel free to customize this to your needs.
#

import os.path
<<<<<<< HEAD
=======
try:
    from sh import CommandNotFound, jshint, cat, ErrorReturnCode_2
    hint = jshint
except (ImportError, CommandNotFound):
    hint = None
>>>>>>> bcd2b063ddbd23b694f6f2dba8060f7238354dd2

top = '.'
out = 'build'

def options(ctx):
    ctx.load('pebble_sdk')

def configure(ctx):
    ctx.load('pebble_sdk')

def build(ctx):
<<<<<<< HEAD
=======
    if False and hint is not None:
        try:
            hint([node.abspath() for node in ctx.path.ant_glob("src/**/*.js")], _tty_out=False) # no tty because there are none in the cloudpebble sandbox.
        except ErrorReturnCode_2 as e:
            ctx.fatal("\nJavaScript linting failed (you can disable this in Project Settings):\n" + e.stdout)

    # Concatenate all our JS files (but not recursively), and only if any JS exists in the first place.
    ctx.path.make_node('src/js/').mkdir()
    js_paths = ctx.path.ant_glob(['src/*.js', 'src/**/*.js'])
    if js_paths:
        ctx(rule='cat ${SRC} > ${TGT}', source=js_paths, target='pebble-js-app.js')
        has_js = True
    else:
        has_js = False

>>>>>>> bcd2b063ddbd23b694f6f2dba8060f7238354dd2
    ctx.load('pebble_sdk')

    build_worker = os.path.exists('worker_src')
    binaries = []

    for p in ctx.env.TARGET_PLATFORMS:
        ctx.set_env(ctx.all_envs[p])
        ctx.set_group(ctx.env.PLATFORM_NAME)
<<<<<<< HEAD
        app_elf='{}/pebble-app.elf'.format(ctx.env.BUILD_DIR)
=======
        app_elf='{}/pebble-app.elf'.format(p)
>>>>>>> bcd2b063ddbd23b694f6f2dba8060f7238354dd2
        ctx.pbl_program(source=ctx.path.ant_glob('src/**/*.c'),
        target=app_elf)

        if build_worker:
<<<<<<< HEAD
            worker_elf='{}/pebble-worker.elf'.format(ctx.env.BUILD_DIR)
=======
            worker_elf='{}/pebble-worker.elf'.format(p)
>>>>>>> bcd2b063ddbd23b694f6f2dba8060f7238354dd2
            binaries.append({'platform': p, 'app_elf': app_elf, 'worker_elf': worker_elf})
            ctx.pbl_worker(source=ctx.path.ant_glob('worker_src/**/*.c'),
            target=worker_elf)
        else:
            binaries.append({'platform': p, 'app_elf': app_elf})

    ctx.set_group('bundle')
<<<<<<< HEAD
    ctx.pbl_bundle(binaries=binaries, js=ctx.path.ant_glob('src/js/**/*.js'))
=======
    ctx.pbl_bundle(binaries=binaries, js='pebble-js-app.js' if has_js else [])
    
>>>>>>> bcd2b063ddbd23b694f6f2dba8060f7238354dd2
