# ==========================================
# 나만의 프롬프트 관리 프로그램
# ==========================================

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

prompts = [
    {
        "title": "AI 게임 산업 영향 분석",
        "content": "생성형 AI가 게임 산업에 미치는 영향을 게임 기획자, 개발자, 비즈니스 기획자의 관점에서 분석해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "Home Barista 커피 제품 이미지",
        "content": "프리미엄 스페셜티 커피 원두 패키지를 고급스럽고 따뜻한 분위기의 제품 사진으로 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "베이스온 야구 광고 영상",
        "content": "패배 후 허탈함을 느끼던 야구팬이 다음 경기 선발투수와 팀 전력을 확인하고 다시 기대감을 갖게 되는 10초 광고 영상을 제작해주세요.",
        "category": "영상 생성",
        "favorite": False
    },
    {
        "title": "메이플스토리 이벤트 알림 자동화",
        "content": "메이플스토리 공식 이벤트 페이지에서 새로운 이벤트를 확인하고 Discord 채널에 자동으로 알림을 보내는 자동화 시스템을 구성해주세요.",
        "category": "자동화",
        "favorite": False
    }
]


def show_menu():
    print("\n================================")
    print("       나만의 프롬프트 관리")
    print("================================")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 삭제")
    print("0. 종료")
    print("================================")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비워둘 수 없습니다.")

    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("\n프롬프트가 추가되었습니다!")


def select_category():
    print("\n카테고리 선택")

    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}) {category}")

    print(f"{len(CATEGORIES) + 1}) 직접 입력")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(CATEGORIES):
                return CATEGORIES[number - 1]

            if number == len(CATEGORIES) + 1:
                custom_category = input("새 카테고리 입력: ").strip()

                if custom_category:
                    return custom_category

                print("카테고리는 비워둘 수 없습니다.")
                continue

        print("올바른 카테고리 번호를 입력해주세요.")


def print_prompt_summary(index, prompt):
    favorite = " ⭐" if prompt["favorite"] else ""

    print(
        f"{index}. "
        f"[{prompt['category']}] "
        f"{prompt['title']}"
        f"{favorite}"
    )


def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, 1):
        print_prompt_summary(index, prompt)

    print("※ ⭐ 표시는 즐겨찾기 프롬프트입니다.")
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    category = select_category()

    results = []

    for index, prompt in enumerate(prompts, 1):
        if prompt["category"] == category:
            results.append((index, prompt))

    print(f"\n[{category}] 카테고리 프롬프트:")

    if not results:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for index, prompt in results:
        print_prompt_summary(index, prompt)

    print(f"\n총 {len(results)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip().lower()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for index, prompt in enumerate(prompts, 1):
        title = prompt["title"].lower()
        content = prompt["content"].lower()

        if keyword in title or keyword in content:
            results.append((index, prompt))

    print("\n검색 결과:")

    if not results:
        print("검색 결과가 없습니다.")
        return

    for index, prompt in results:
        print_prompt_summary(index, prompt)

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def get_prompt_number():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None

    while True:
        number = input("프롬프트 번호 입력: ").strip()

        if number.isdigit():
            index = int(number)

            if 1 <= index <= len(prompts):
                return index - 1

        print("올바른 프롬프트 번호를 입력해주세요.")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    index = get_prompt_number()

    if index is None:
        return

    prompt = prompts[index]

    favorite = "⭐" if prompt["favorite"] else "없음"

    print("\n--------------------------------")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite}")
    print("--------------------------------")
    print("내용:")
    print(prompt["content"])
    print("--------------------------------")


def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    index = get_prompt_number()

    if index is None:
        return

    prompt = prompts[index]

    if prompt["favorite"]:
        prompt["favorite"] = False
        print(
            f"'{prompt['title']}' 프롬프트의 "
            "즐겨찾기를 해제했습니다."
        )
    else:
        prompt["favorite"] = True
        print(
            f"'{prompt['title']}' 프롬프트를 "
            "즐겨찾기에 추가했습니다!"
        )


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorites = []

    for index, prompt in enumerate(prompts, 1):
        if prompt["favorite"]:
            favorites.append((index, prompt))

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for index, prompt in favorites:
        print_prompt_summary(index, prompt)

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def delete_prompt():
    print("\n=== 프롬프트 삭제 ===")

    index = get_prompt_number()

    if index is None:
        return

    prompt = prompts[index]

    confirm = input(
        f"'{prompt['title']}' 프롬프트를 삭제하시겠습니까? (y/n): "
    ).strip().lower()

    if confirm == "y":
        deleted_title = prompt["title"]
        prompts.pop(index)
        print(f"'{deleted_title}' 프롬프트가 삭제되었습니다.")
    else:
        print("삭제를 취소했습니다.")


def main():
    while True:
        show_menu()

        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()

        elif choice == "2":
            show_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_detail()

        elif choice == "6":
            manage_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "8":
            delete_prompt()

        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break

        else:
            print("\n잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()