
import styles from './page.module.css'
import NotificationForm from './components/form'
import NotificationHistory from './components/notificationHistory'

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <NotificationForm/>
        <NotificationHistory />
      </div>
    </main>
  )
}
