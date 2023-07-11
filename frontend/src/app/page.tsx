
import styles from './page.module.css'
import NotificationForm from './components/form'
import LogHistory from './components/logHistory'

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <NotificationForm/>
        <LogHistory />
      </div>
    </main>
  )
}
