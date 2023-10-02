from pico2d import *

# 코딩 요령
# 먼저 전체적인 뼈대 제작 후 세부적인 내용
# 테스트 리드 타임을 줄인다.
# 조금씩 살을 붙여감.
# 조그마한 진전이 있으면 commit 한다.
# 코드가 길어지거나 재사용의 필요성이 생기면 함수를 만든다.
# 변수 이름, 함수 이름 구체적 작성

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():
    global TUK_ground, character
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, x, y, frame
    running = True
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()


def update_world():
    global frame
    frame = (frame + 1) % 8


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()  # 초기화

while running:
    render_world()  # world의 현재 내용을 그린다.
    handle_events()  # 사용자 입력을 받아들인다.
    update_world()  # world안의 객체들의 상호작용을 계산하고 그 결과를 update 한다.

close_canvas()
