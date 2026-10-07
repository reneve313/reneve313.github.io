# 글과 프로젝트 추가하기

현재 화면의 모든 글과 프로젝트는 미리보기용 예시입니다. about 원본은 변경하지 않았습니다.

## Topics

`_posts/YYYY-MM-DD-slug.md` 파일을 추가합니다. 기존 예시 글을 복사하고 제목, 날짜, 본문을 바꾸면 됩니다.

```yaml
---
layout: post
title: "새로운 공부 기록"
description: "글을 한 줄로 소개합니다."
date: 2026-10-07 09:00:00 +0900
subject: Security
tags: [Web, Security]
related_posts: false
---
```

본문 위에 `[← topics로 돌아가기]({{ '/topics/' | relative_url }})`를 추가할 수 있습니다.
`subject` 값으로 Topics의 주제 버튼이 자동 생성됩니다. 미래 날짜의 글은 기본적으로 표시되지 않습니다.
실제 글을 쓸 때는 샘플의 `sample: true`와 인용문 형태의 예시 안내를 제거하세요.

## Projects

`_projects/`의 예시 HTML 파일을 복사합니다. 머리말의 `title`, `description`, `permalink`, `project_key`, `icon`, `stack`을 수정합니다.
`status: ongoing`이면 진행 중, `status: completed`이면 완료 구역에 나타납니다. `importance`가 작을수록 먼저 표시됩니다.
아이콘은 `icon` 필드의 문자로 표시되고, 카드 전체를 클릭할 수 있습니다.
실제 프로젝트를 등록할 때는 예시 파일의 `sample: true`와 샘플 안내를 제거하세요.

## 프로젝트별 글

`_project_notes/프로젝트키/글이름.md`를 추가합니다.
`project` 값은 프로젝트의 `project_key`와 같아야 합니다. 날짜가 최신인 글부터 자동 정렬됩니다.

```yaml
---
layout: post
title: "프로젝트 첫 기록"
description: "이번에 진행한 내용을 정리합니다."
date: 2026-10-07 09:00:00 +0900
project: security-lab
stage: 개발 노트
related_posts: false
---
```

본문 위의 돌아가기 링크도 해당 프로젝트 주소로 지정하세요.

## Extra: 취미와 일상

`_extra/글이름.md`에 글을 추가합니다. `_extra/`의 예시를 복사해 제목, 설명, 날짜, 본문을 바꾸세요.
`subject`는 주제 버튼(예: 일상, 음악, 영화), `tags`는 글의 키워드, `motif`는 목록에 표시할 이모지입니다.
실제 글에서는 `sample: true`와 미리보기 안내를 지웁니다. 글은 `/extra/글이름/` 주소로 생성되고 Topics와 별도로 모입니다.
본문의 `[← extra로 돌아가기]({{ '/extra/' | relative_url }})` 링크를 유지하면 목록으로 돌아갈 수 있습니다.

## 미리보기 실행

Docker Desktop을 켜고 저장소 폴더에서 `docker compose up -d`를 실행합니다.
http://localhost:8080/topics/ 와 http://localhost:8080/projects/ 에서 확인합니다.
페이지와 글은 저장하면 자동 반영됩니다. `_config.yml` 변경이 반영되지 않으면 `docker compose restart`를 실행하세요.
검토 전에는 커밋하거나 푸시하지 않습니다.
