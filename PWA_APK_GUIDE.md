# PWA를 APK로 변환하는 방법

## PWA 테스트 방법

1. **크롬 브라우저에서 PWA 테스트:**
   - http://localhost:3000 접속
   - F12 키를 눌러 개발자 도구 열기
   - Application 탭 선택
   - Service Workers 섹션에서 Service Worker 등록 확인
   - Manifest 섹션에서 manifest.json 로드 확인

2. **PWA 설치 테스트:**
   - 크롬 주소창 오른쪽 끝의 설치 아이콘 클릭
   - 또는 페이지 상단의 "앱 설치" 버튼 클릭
   - 설치 후 바탕화면이나 앱 목록에서 앱 실행

## APK 생성 방법

### 방법 1: PWA Builder 사용 (권장)

1. **사이트 배포:**
   - Vercel, Netlify 등에 배포하여 HTTPS URL 획득
   
2. **PWA Builder 접속:**
   - https://www.pwabuilder.com/ 접속
   - 배포된 사이트 URL 입력
   - "Start" 클릭

3. **APK 다운로드:**
   - 분석 완료 후 "Package for stores" 클릭
   - "Android" 선택
   - 옵션 설정:
     - Package ID: com.retriever.app
     - App name: Retriever
     - Version: 1.0.0
   - "Download" 클릭하여 APK 파일 다운로드

### 방법 2: Bubblewrap 사용

1. **Node.js 및 Java 설치 확인:**
   ```bash
   node --version
   java --version
   ```

2. **Bubblewrap CLI 설치:**
   ```bash
   npm install -g @bubblewrap/cli
   ```

3. **프로젝트 초기화:**
   ```bash
   mkdir retriever-android
   cd retriever-android
   bubblewrap init --manifest https://your-deployed-site.com/manifest.json
   ```

4. **APK 빌드:**
   ```bash
   bubblewrap build
   ```

5. **생성된 APK 파일 확인:**
   - `app-release-signed.apk` 파일이 생성됨

### 방법 3: Android Studio + TWA 사용

1. **Android Studio 설치**

2. **Trusted Web Activity 프로젝트 생성:**
   - New Project > Empty Activity
   - Package name: com.retriever.app

3. **build.gradle 수정:**
   ```gradle
   dependencies {
       implementation 'com.google.androidbrowserhelper:androidbrowserhelper:2.5.0'
   }
   ```

4. **AndroidManifest.xml 설정:**
   ```xml
   <activity android:name="com.google.androidbrowserhelper.trusted.LauncherActivity">
       <meta-data android:name="android.support.customtabs.trusted.DEFAULT_URL"
                  android:value="https://your-site.com" />
       <intent-filter>
           <action android:name="android.intent.action.MAIN" />
           <category android:name="android.intent.category.LAUNCHER" />
       </intent-filter>
   </activity>
   ```

5. **Build > Build Bundle(s) / APK(s) > Build APK(s)**

## APK 설치 방법

### Android 기기에서:
1. APK 파일을 기기로 전송
2. 파일 관리자에서 APK 파일 실행
3. "출처를 알 수 없는 앱 설치" 허용
4. 설치 진행

### 에뮬레이터에서:
```bash
adb install retriever.apk
```

## 주의사항

- **HTTPS 필수:** PWA는 보안상 HTTPS에서만 완전히 작동합니다
- **아이콘 최적화:** 512x512 아이콘은 필수입니다
- **오프라인 지원:** Service Worker가 제대로 작동하는지 확인하세요
- **성능:** Lighthouse로 PWA 점수를 확인하세요 (90점 이상 권장)

## 현재 구현된 기능

✅ Service Worker 등록 및 캐싱
✅ 오프라인 지원
✅ 설치 가능한 PWA
✅ 아이콘 및 스플래시 스크린
✅ 독립 실행형 앱 모드
✅ 채팅 및 크롤링 기능 유지

## 배포 추천 서비스

1. **Vercel** (Next.js 최적화)
   ```bash
   npm install -g vercel
   vercel
   ```

2. **Netlify**
   ```bash
   npm install -g netlify-cli
   netlify deploy
   ```

3. **Firebase Hosting**
   ```bash
   npm install -g firebase-tools
   firebase init hosting
   firebase deploy
   ```

배포 후 HTTPS URL을 사용하여 위의 APK 생성 방법 중 하나를 선택하세요.