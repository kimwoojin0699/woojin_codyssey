# Docker 명령어 정리

## 🐳 Docker 기본 명령어

| 명령어 | 설명 |
|--------|------|
| `docker --version` | Docker 버전 확인 |
| `docker info` | Docker 시스템 정보 확인 |
| `docker help` | 명령어 도움말 보기 |

---

## 🛠️ 이미지 관련 명령어

| 명령어 | 설명 |
|--------|------|
| `docker images` | 로컬에 저장된 이미지 목록 보기 |
| `docker pull [이미지명]` | 이미지 다운로드 |
| `docker build -t [이미지이름] .` | Dockerfile 기반 이미지 생성 |
| `docker rmi [이미지ID]` | 이미지 삭제 |
| `docker tag [이미지ID] [새이름]` | 이미지 태그 변경 |

---

## 📦 컨테이너 관련 명령어

| 명령어 | 설명 |
|--------|------|
| `docker ps` | 실행 중인 컨테이너 목록 보기 |
| `docker ps -a` | 모든 컨테이너 보기 (종료 포함) |
| `docker run [옵션] [이미지명]` | 컨테이너 실행 |
| `docker start [컨테이너ID]` | 정지된 컨테이너 실행 |
| `docker stop [컨테이너ID]` | 컨테이너 정지 |
| `docker restart [컨테이너ID]` | 컨테이너 재시작 |
| `docker rm [컨테이너ID]` | 컨테이너 삭제 |
| `docker exec -it [컨테이너ID] bash` | 실행 중인 컨테이너에 접속 (bash 쉘) |

---

## 📂 볼륨 / 네트워크 / 로그

| 명령어 | 설명 |
|--------|------|
| `docker volume ls` | 볼륨 목록 보기 |
| `docker volume rm [볼륨명]` | 볼륨 삭제 |
| `docker network ls` | 네트워크 목록 보기 |
| `docker logs [컨테이너ID]` | 컨테이너 로그 출력 |

---

## 🧹 시스템 정리

| 명령어 | 설명 |
|--------|------|
| `docker system prune` | 사용하지 않는 이미지, 컨테이너, 볼륨 정리 |
| `docker container prune` | 중지된 컨테이너만 정리 |
| `docker image prune` | 사용하지 않는 이미지 정리 |

---

## 🐳 Docker Compose 관련

| 명령어 | 설명 |
|--------|------|
| `docker-compose up` | docker-compose.yml로 컨테이너 실행 |
| `docker-compose down` | 모든 서비스 중단 및 정리 |
| `docker-compose ps` | 실행 중인 서비스 확인 |
| `docker-compose logs` | 서비스 로그 확인 |

---

## 🔍 기타 유용한 옵션

- `-d`: 백그라운드 모드
- `--name`: 컨테이너 이름 지정
- `-p`: 포트 바인딩 (예: `-p 8080:80`)
- `-v`: 볼륨 마운트 (예: `-v ./data:/app/data`)
